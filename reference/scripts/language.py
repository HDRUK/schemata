# Script that generates the spatial.json file, 
# with ISO 639 codes.

import requests
import json
from pathlib import Path

ISO_639_URL = ("https://salsa.debian.org/iso-codes-team/iso-codes/-/raw/"
                    "main/data/iso_639-2.json")

BASE_PATH = Path(__file__).parent

def fetch_data(url):
    r = requests.get(url)
    return r.json()


def main():
    # Fetch ISO 639 codes from the web
    iso_639_2 = fetch_data(ISO_639_URL)
    
    # Build output file header
    out = {
        "title": "Language Codes Reference Data",
        "description": "ISO 3166-1 and ISO 3166-2 codes.",
        "enumerations": []
        }

    # Add ISO 639-1 codes to enumerations
    iso_639_2_codes = [
        l.get('alpha_2') for l in iso_639_2['639-2'] if l.get('alpha_2')
        ]
    
    out['enumerations'].extend(iso_639_2_codes)

    # Write output file
    filepath = (BASE_PATH / '../data/iso_639.json').resolve()
    with open(filepath, 'w') as f:
        json.dump(out, f, indent=2)

if __name__ == '__main__':
    main()
    print("Done.")