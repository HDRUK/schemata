#!/bin/bash
cd hdr_schemata/models/HDRUK
python create_json_schema.py 
cd ../GWDM
python create_json_schema.py 

cd ../../../


python hdr_schemata/utils/create_markdown.py
