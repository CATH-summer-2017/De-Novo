#!/usr/bin/python3
import json
import requests
from pprint import pprint
json_origin_file = open('/home/ilya/Projects/De-Novo/De-Novo-PDB.json', 'r')
protein_list = []
for protein in json.loads(json_origin_file.read())['grouped']['pdb_id']['groups']:
    protein_list.append(protein['groupValue'])
dict_of_pdb = {}
u_a = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
def get_superfam(pdb_id):
    res = requests.get('http://www.cathdb.info/version/v4_1_0/api/rest/domain_summary/' + pdb_id + 'A00/', headers={"USER-AGENT":u_a})
    json_soup = res.json()
    if json_soup["success"] == False:
        print("No superfam for this domain")
    if json_soup["success"] == True:
        print("Will need to get a chopping for this")
        dict_of_pdb[pdb_id] = json_soup['data']['superfamily_id']

for protein in protein_list:
    print(protein)
    get_superfam(protein)
pprint(dict_of_pdb)


# results
# {'2a3d': '1.20.58.130',
#  '2mra': '3.30.1710.10',
#  '3hoj': '3.20.20.70',
#  '3nxf': '3.20.20.70',
#  '3o49': '2.80.10.50',
#  '3o4a': '2.80.10.50',
#  '3o4b': '2.80.10.50',
#  '3o4c': '2.80.10.50',
#  '3o4d': '2.80.10.50',
#  '3ud6': '3.20.20.70',
#  '3v1a': '4.10.860.20',
#  '3v1b': '4.10.860.20',
#  '3v1c': '4.10.860.20',
#  '3v1d': '4.10.860.20',
#  '3v1e': '4.10.860.20',
#  '3v1f': '4.10.860.20',
#  '4d8h': '2.80.10.50',
#  '4ess': '3.40.220.10',
#  '4etj': '3.40.220.10',
#  '4etk': '3.40.220.10',
#  '4f2v': '3.30.572.10',
#  '4f34': '2.80.10.50',
#  '4gmr': '1.25.40.20',
#  '4hxt': '1.25.10.10',
#  '4kyb': '3.40.220.10',
#  '4loa': '3.40.50.300'}
