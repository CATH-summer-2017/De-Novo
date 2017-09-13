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
# u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
# response = requests.get(url, headers={"USER-AGENT":u_a})


# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}
# >>> _get = get('http://stats.nba.com/stats/playergamelog', params={'PlayerID': 203082, 'Season':'2015-16', 'SeasonType':'Regular Season'}, headers=headers)
# >>> _get.raise_for_status()
