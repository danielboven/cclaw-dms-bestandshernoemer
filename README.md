# CClaw DMS bestandshernoemer

Het softwarepakket CClaw bevat een documentmanagementsysteem (DMS). De bestanden in het DMS worden opgeslagen onder unieke IDs (UUIDs) met als gevolg dat de originele bestandsnaam ontbreekt in de bestandsstructuur. Door de database van het DMS te koppelen aan de individuele bestanden kan de originele naam worden hersteld.

Deze Python-tool helpt om de transformatie van de bestandsnamen uit het DMS uit te voeren.

## Snelle start

**1. Installeren**

Het is aan te raden om eerst een nieuwe virtuele omgeving in Python aan te maken:

	python -m venv mijnomgeving

Activeer nu de omgeving. Dit kan in het Windows commandoprompt als volgt:

	mijnomgeving\Scripts\activate.bat
	
Of in een PowerShell omgeving:
	
	mijnomgeving\Scripts\Activate.ps1

Haal vervolgens de benodigde bestanden op van GitHub:

	git clone https://github.com/danielboven/cclaw-dms-bestandshernoemer.git
	cd cclaw-dms-bestandshernoemer

Installeer de vereiste Python-pakketten:

	pip install -r requirements.txt

**2. In gebruik nemen** (met behulp van een demo)

	python bestandshernoemer.py demo/database_dms.json demo/DOSSIERS -x "Thumbs.db" -x "~$*"

## CLI gebruik

Hulp voor de CLI-applicatie kan worden verkregen door het script te starten met de `-h` optie.

```
$ python bestandshernoemer.py -h
usage: bestandshernoemer.py [-h] [-x X [X ...]] database_dms dossiers

positional arguments:
  database_dms  Het JSON-bestand dat de verwijzingen naar de bestanden uit het DMS bevat.
  dossiers      De DOSSIERS map die alle bestanden uit het DMS bevat.

options:
  -h, --help    show this help message and exit
  -x X [X ...]  Uitsluitingspatroon om bestanden uit het DMS te verwijderen.
```

## CLI parameters

### Verplichte positionele parameters

| Positionele parameter | Toelichting |
| -- | -- |
| database_dms | Het JSON-bestand dat de verwijzingen naar de bestanden uit het DMS bevat. Dit bestand kan worden geëxporteerd  vanuit de database m.b.v. DBeaver. |
| dossiers | De **DOSSIERS** map die alle bestanden uit het DMS bevat. Kopieer deze map vanaf de installatiemap van CClaw & DMS op de server. |

### Opties

`-x` is een optie om een uitsluitingspatroon aan te geven. Op basis van het patroon worden bestanden uit de map **DOSSIERS** verwijderd.

Het uitsluitingspatroon helpt om de bestandsstructuur op te schonen.
Bestanden die eigenlijk niet in het DMS hadden moeten staan, zoals `Thumbs.db` of tijdelijke Office-bestanden (`~$-brief.docx`) kunnen hiermee als volgt verwijderd worden:

	-x "Thumbs.db" -x "~$*"
	
De asterisk fungeert als wildcard voor één of meer karakters (inclusief bestandsextensie).

## JSON-bestand van DMS-database exporteren

Verbind met de DMS-database in [DBeaver](https://dbeaver.io/). Dit kan door met de live database te verbinden op de server, of een back-up (BAK-bestand) in te laden [in de SQL Server Management Studio](https://stackoverflow.com/a/30338131).

Navigeer in DBeaver naar de tabel genaamd **Documenten** en exporteer deze tabel naar een JSON-bestand met behulp van de [Data Transfer](https://dbeaver.com/docs/wiki/Data-transfer) functie in DBeaver.

Gebruik het verkregen JSON-bestand als parameter voor `database_dms`.

## Licentie
[MIT](https://choosealicense.com/licenses/mit/)
