import glob
import json

structure = {}
for schema in glob.glob('metadata/**/schema.json',recursive=True):
    items = schema.split('/')
    model = items[1]
    version = items[2]
    if model not in structure:
        structure[model] = []
    structure[model].append(version)

json.dump(structure,open('available.json','w'),indent=6)
