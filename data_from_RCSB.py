#!/usr/bin/python3
import requests
from pprint import pprint
proteins = ["1BB1", "1E0M", "1UW1", "2BKG", "2JAB", "2JGO", "2JWS", "2JWU", "2K6R", "2KJN", "2KJO", "2KL8", "2KOZ", "2KP0", "2KPO", "2L69", "2L82", "2L96", "2L99", "2L9A", "2LCI", "2LHC", "2LHD", "2LHE", "2LHG", "2LN3", "2LND", "2LNY", "2LQ4", "2LR0", "2LR2", "2LRH", "2LSE", "2LTA", "2LV8", "2LVB", "2LZE", "2MBL", "2MBM", "2MDV", "2MDW", "2MI7", "2MLB", "2MN4", "2MQ8", "2MR5", "2MR6", "2MRA", "2MTL", "2MTT", "2MTU", "2MUZ", "2N35", "2N3Z", "2N41", "2N4E", "2N4N", "2N63", "2N65", "2N75", "2N76", "2N8D", "2N8I", "2N8W", "2NBL", "2ND2", "2ND3", "2RU4", "2RU5", "2RVD", "2X6P", "2XEE", "2XEH", "2XEN", "3HE4", "3HE5", "3LT8", "3LT9", "3LTA", "3LTB", "3LTC", "3LTD", "3M22", "3M24", "3MIP", "3MIS", "3O49", "3O4A", "3O4B", "3O4C", "3O4D", "3OGF", "3OL0", "3P46", "3PBJ", "3PG0", "3S0R", "3TDM", "3TDN", "3TQ2", "3V1A", "3V1B", "3V1C", "3V1D", "3V1E", "3V1F", "3VB8", "3VJF", "4A29", "4D49", "4D4E", "4D8H", "4DB6", "4DB8", "4DB9", "4DBA", "4DRT", "4DUI", "4DZU", "4DZV", "4ESS", "4ETJ", "4F2V", "4GMR", "4GPM", "4H7R", "4H8F", "4H8G", "4H8L", "4H8M", "4H8O", "4HB5", "4HQD", "4HXT", "4IJB", "4IVH", "4J7W", "4J8Y", "4JW2", "4KY3", "4KYB", "4KYV", "4KYZ", "4LNY", "4LOA", "4LPT", "4LPU", "4LPV", "4LPW", "4LPX", "4LPY", "4LT9", "4M6A", "4N6T", "4N6U", "4NEY", "4NEZ", "4NTP", "4NTR", "4NW8", "4NW9", "4O60", "4OW4", "4OXW", "4P4V", "4P4W", "4P4X", "4P4Y", "4P4Z", "4P6J", "4P6K", "4P6L", "4PN8", "4PN9", "4PNA", "4PND", "4PQ8", "4PSJ", "4PWW", "4QFV", "4QKR", "4QKS", "4R58", "4R5C", "4R5D", "4R6F", "4R6G", "4R6J", "4R80", "4RJV", "4RV1", "4RZP", "4TQL", "4TUT", "4U3H", "4UBY", "4UBZ", "4UOS", "4UOT", "4V3O", "4V3Q", "4V3R", "4W5L", "4W5M", "4W5P", "4W5Y", "4W67", "4W71", "4WBU", "4WBV", "4WSL", "4YDW", "4YFO", "4YXX", "4YXY", "4YXZ", "4YY2", "4YY5", "4Z08", "4ZCN", "4ZV6", "5A0O", "5AEI", "5AWL", "5BVB", "5BVL", "5BYO", "5C39", "5CHB", "5CW9", "5CWB", "5CWC", "5CWD", "5CWF", "5CWG", "5CWH", "5CWI", "5CWJ", "5CWK", "5CWL", "5CWM", "5CWN", "5CWO", "5CWP", "5CWQ", "5D2T", "5D2V", "5D2W", "5D2X", "5D2Y", "5D30", "5D32", "5D33", "5D37", "5D38", "5DI5", "5DN0", "5DNS", "5DQA", "5DRA", "5DXV", "5DZB", "5E6G", "5EHB", "5EIL", "5EOJ", "5EON", "5ET3", "5EZ8", "5EZ9", "5EZA", "5EZC", "5EZE", "5F2Y", "5F53", "5GAJ", "5HKN", "5HKR", "5HPN", "5HRY", "5HRZ", "5HS0", "5I1Y", "5I1Z", "5IEN", "5IEO", "5IEP", "5IER", "5IF6", "5IZS", "5J0H", "5J0I", "5J0J", "5J0K", "5J0L", "5J10", "5J2L", "5J73", "5J7D", "5JG9", "5JHI", "5JI4", "5JQZ", "5K7V", "5K92", "5KB0", "5KB1", "5KB2", "5KBA", "5KKG", "5KNG", "5KPE", "5KPH", "5KVN", "5KWO", "5KWP", "5KWX", "5KWZ", "5KX0", "5KX1", "5KX2", "5L2H", "5L33", "5LE2", "5LE3", "5LE4", "5LE6", "5LE7", "5LE8", "5LE9", "5LEA", "5LEB", "5LEC", "5LED", "5LEE", "5LW2", "5MFB", "5MFE", "5MFF", "5MFG", "5MFH", "5MFI", "5MFJ", "5MFK", "5MFL", "5MFN", "5MFO", "5TPH", "5TPJ", "5TRV", "5TS4", "5U35", "5U59", "5U5A", "5U5B", "5U5C", "5U9T", "5U9U", "5UXT", "5V63", "5V64", "5V65", "5VBT", "5WRX", "5XG5"]
dict_of_pdb = {}
protein_list = []
for prot in proteins:
    protein_list.append(prot.lower())
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
# {'2bkg': '1.25.40.20',
#  '2jab': '1.25.40.20',
#  '2jws': '1.10.8.40',
#  '2jwu': '3.10.20.10',
#  '2lhc': '1.10.8.40',
#  '2lhd': '3.10.20.10',
#  '2lhe': '3.10.20.10',
#  '2lhg': '1.10.8.40',
#  '2mlb': '3.10.20.90',
#  '2mn4': '1.10.533.10',
#  '2mra': '3.30.1710.10',
#  '2xee': '1.25.40.20',
#  '2xeh': '1.25.40.20',
#  '2xen': '1.25.40.20',
#  '3mip': '3.10.28.10',
#  '3mis': '3.10.28.10',
#  '3o49': '2.80.10.50',
#  '3o4a': '2.80.10.50',
#  '3o4b': '2.80.10.50',
#  '3o4c': '2.80.10.50',
#  '3o4d': '2.80.10.50',
#  '3pg0': '2.80.10.50',
#  '3v1a': '4.10.860.20',
#  '3v1b': '4.10.860.20',
#  '3v1c': '4.10.860.20',
#  '3v1d': '4.10.860.20',
#  '3v1e': '4.10.860.20',
#  '3v1f': '4.10.860.20',
#  '4a29': '3.20.20.70',
#  '4d8h': '2.80.10.50',
#  '4db6': '1.25.10.10',
#  '4db8': '1.25.10.10',
#  '4db9': '1.25.10.10',
#  '4dba': '1.25.10.10',
#  '4dui': '1.25.40.20',
#  '4ess': '3.40.220.10',
#  '4etj': '3.40.220.10',
#  '4f2v': '3.30.572.10',
#  '4gmr': '1.25.40.20',
#  '4gpm': '1.25.40.20',
#  '4hb5': '1.25.40.20',
#  '4hqd': '1.25.40.20',
#  '4hxt': '1.25.10.10',
#  '4ijb': '3.20.20.70',
#  '4j7w': '1.25.40.20',
#  '4j8y': '1.25.40.20',
#  '4kyb': '3.40.220.10',
#  '4kyv': '3.40.50.1820',
#  '4lny': '3.20.20.70',
#  '4loa': '3.40.50.300',
#  '4lpu': '2.60.40.10',
#  '4lt9': '3.20.20.70',
#  '4n6t': '3.10.450.10',
#  '4n6u': '3.10.450.10',
#  '4ow4': '2.80.10.50',
#  '4pq8': '3.80.10.10',
#  '4psj': '3.80.10.10'}
