import os, json, re, argparse
from progress.bar import Bar

parser = argparse.ArgumentParser()
parser.add_argument('database_dms', type=str, help='Het JSON-bestand dat de verwijzingen naar de bestanden uit het DMS bevat.')
parser.add_argument('dossiers', type=str, help='De DOSSIERS map die alle bestanden uit het DMS bevat.')
parser.add_argument('-x', type=str, action='append', nargs='+', required=False, help='Uitsluitingspatroon om bestanden uit het DMS te verwijderen.')

args = parser.parse_args()

# Define list with patterns to exclude files
exluded = [i[0] for i in args.x] if args.x else []

with open(args.database_dms, encoding='utf-8') as json_file:
    data = json.load(json_file)
    bar = Bar('Bestanden hernoemen', max = len(data['Documenten']))
    
    for i, document in enumerate(data['Documenten']):
        # Continue progress bar
        bar.next()
        
        location = document['BESTANDS_LOCATIE']
        
        # Fix location names in database starting with \
        if location.startswith('\\'):
            location = location.replace('\\', '', 1)
        
        folder, uuid = location.split("\\", 1)
        filename, file_extension = os.path.splitext(document['BESTANDS_NAAM'])
        filename = filename.replace('\\', ' ').replace('—', '-') # Fix unsupported characters inside filename
        filename = re.sub(' +', ' ', filename.strip()) # Remove multiple spaces and strip begin & end spaces
        current_path = os.path.join(args.dossiers, folder, uuid)
        new_path = os.path.join(args.dossiers, folder, filename + file_extension)
        
        if not os.path.exists(current_path):
            continue
            
        # Exclude file based on pattern matching
        is_match = False
        
        for exclude in exluded:
            regex = re.escape(exclude).replace('\*', '.*')
            matched = re.match(regex, filename + file_extension)
            is_match = bool(matched) if not is_match else True
            
        # Remove file from DMS if it matches pattern
        if is_match:
            os.remove(current_path)
            continue
        
        # Handle a file with a name that already exists
        postfix = 1

        while os.path.exists(new_path):
            postfix += 1
            new_path = os.path.join(
                args.dossiers,
                folder,
                filename + ' (' + str(postfix) + ')' + file_extension
            )

        # Rename UUID file to original name from DMS database
        os.rename(current_path, new_path)
