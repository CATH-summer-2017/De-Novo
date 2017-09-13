#!/usr/bin/python3
import json
json_origin_file = open('/home/ilya/Projects/De-Novo/De-Novo-PDB.json', 'r')
protein_list = []
for protein in json.loads(json_origin_file.read())['grouped']['pdb_id']['groups']:
    protein_list.append(protein['groupValue'])
print(protein_list)
