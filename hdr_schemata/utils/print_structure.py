import glob
import json

structure = {}
for schema in glob.glob('hdr_schemata/models/**/schema.json',recursive=True):
    items = schema.split('/')
    model = items[2]
    version = items[3]
    if model not in structure:
        structure[model] = []
    structure[model].append(version)

json.dump(structure,open('available.json','w'),indent=6)
