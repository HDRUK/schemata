# Script that generates the spatial.json file, 
# with ISO 3166-1 and ISO 3166-2 codes.

import requests
import json
import csv
from pathlib import Path

ISO_3166_1_URL = ("https://salsa.debian.org/iso-codes-team/iso-codes/-/raw/"
                    "main/data/iso_3166-1.json")
ISO_3166_2_URL = ("https://salsa.debian.org/iso-codes-team/iso-codes/-/raw/"
                    "main/data/iso_3166-2.json")

BASE_PATH = Path(__file__).parent

def fetch_data(url):
    r = requests.get(url)
    return r.json()

def read_csv(filepath):
    rows = []
    with open(filepath, 'r', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
    return rows

def write_to_reference(filename, title, description, enumerations):
    out = {
        "title": title,
        "description": description,
        "enumerations": enumerations
        }

    filepath = (BASE_PATH / filename).resolve()

    with open(filepath, 'w') as f:
        json.dump(out, f, indent=2)


def main():
    # Fetch ISO 3166 codes from the web
    iso_3166_1_data = fetch_data(ISO_3166_1_URL)
    iso_3166_2_data = fetch_data(ISO_3166_2_URL)
    
    # Read in the CSV file with ONS codes
    filepath = (BASE_PATH / '../resources/IPN_GB_2021.csv').resolve()
    ons_data = read_csv(filepath=filepath)


    # Build output file for ISO 3166-1
    iso_3166_1_codes = [c['alpha_2'] for c in iso_3166_1_data['3166-1']]
    
    write_to_reference(
        filename = '../data/iso_3166-1.json',
        title = 'ISO 3166-1 Codes',
        description = 'To be used spatial coverage of datasets.',
        enumerations=iso_3166_1_codes
        )

    # Build output file for ISO 3166-2
    iso_3166_2_codes = [c['code'] for c in iso_3166_2_data['3166-2']]
    write_to_reference(
        filename = '../data/iso_3166-2.json',
        title = 'ISO 3166-2 Codes',
        description = 'To be used spatial coverage of datasets.',
        enumerations=iso_3166_2_codes
        )

    # Build output file for ONS codes
    ons_codes = [c['place20cd'] for c in ons_data]
    write_to_reference(
        filename = '../data/ons_codes.json',
        title = 'ONS Codes Place Name Codes',
        description = 'To be used spatial coverage of datasets.',
        enumerations=ons_codes
        )

if __name__ == '__main__':
    main()
    print("Done.")
