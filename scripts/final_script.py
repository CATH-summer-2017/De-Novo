#!/usr/bin/python3
import re
from pprint import pprint
import json
proteins = ["1BB1", "1BYZ", "1C3T", "1CQ0", "1D7T", "1DJF", "1DN3", "1DNG", "1E0M", "1EC5", "1FME", "1G6U", "1HQJ", "1IC9", "1ICL", "1ICO", "1IHQ", "1J4M", "1JM0", "1JMB", "1JY4", "1JY6", "1JY9", "1K09", "1K43", "1KD8", "1KD9", "1KDD", "1KVF", "1KVG", "1KYC", "1L2Y", "1L4X", "1LB7", "1LE0", "1LE1", "1LQ7", "1LT1", "1M02", "1M3W", "1MFT", "1MJ0", "1MV4", "1N09", "1N0A", "1N0C", "1N0D", "1NA0", "1NA3", "1OVR", "1OVU", "1OVV", "1P68", "1PBZ", "1Q7O", "1QP6", "1QYS", "1R9V", "1RGR", "1RIJ", "1RIK", "1RIM", "1RVS", "1S1O", "1S4A", "1S9Z", "1SN9", "1SNA", "1SNE", "1SVX", "1T8J", "1TGG", "1TJB", "1U0I", "1U7J", "1U7M", "1UAO", "1UW1", "1VJQ", "1VL3", "1VRZ", "1XOF", "1Y47", "1Y4C", "1Y66", "1YOD", "1YT6", "1YWT", "1YYJ", "1YYX", "1ZSZ", "2AF5", "2AG3", "2AHP", "2AVP", "2BKG", "2CW1", "2DX2", "2DX3", "2DX4", "2E4E", "2EVQ", "2FKG", "2FKJ", "2FO7", "2G6U", "2GJF", "2GJH", "2H3S", "2H3T", "2H4B", "2HKD", "2HYZ", "2HZ8", "2I5V", "2I5Z", "2I7U", "2I9M", "2I9N", "2I9O", "2IGR", "2JAB", "2JGO", "2JO4", "2JO5", "2JOF", "2JRE", "2JST", "2JUA", "2JVF", "2JWS", "2JWU", "2K6R", "2K76", "2KFQ", "2KI0", "2KIK", "2KJN", "2KJO", "2KL8", "2KLW", "2KOZ", "2KP0", "2KPO", "2L69", "2L6B", "2L82", "2L96", "2L99", "2L9A", "2LCH", "2LCI", "2LDA", "2LDC", "2LDD", "2LDJ", "2LFD", "2LFF", "2LHC", "2LHD", "2LHE", "2LHG", "2LL5", "2LN3", "2LND", "2LNY", "2LQ4", "2LR0", "2LR2", "2LRH", "2LSE", "2LTA", "2LU6", "2LUF", "2LV8", "2LVB", "2LXO", "2LXY", "2LZE", "2M0X", "2M7C", "2M7D", "2MBL", "2MBM", "2MDV", "2MDW", "2MG4", "2MH1", "2MI7", "2MLB", "2MN4", "2MQ8", "2MR5", "2MR6", "2MRA", "2MTL", "2MTQ", "2MTT", "2MTU", "2MUZ", "2N08", "2N09", "2N0I", "2N0N", "2N35", "2N3Z", "2N41", "2N4E", "2N4N", "2N63", "2N65", "2N6H", "2N6I", "2N75", "2N76", "2N7N", "2N7O", "2N7T", "2N8B", "2N8C", "2N8D", "2N8I", "2N8W", "2NAY", "2NBL", "2ND2", "2ND3", "2NDL", "2O0S", "2O6N", "2OBG", "2ORU", "2OTK", "2P05", "2P09", "2P0X", "2P6J", "2Q33", "2QYJ", "2R2V", "2RT4", "2RU4", "2RU5", "2RVD", "2WQH", "2X6P", "2XEE", "2XEH", "2XEN", "2ZGD", "2ZGG", "3BX7", "3BX8", "3C3F", "3C3G", "3C3H", "3CAY", "3CBA", "3CSB", "3CSG", "3CWO", "3DGL", "3DGM", "3DGN", "3DGO", "3H5F", "3H5G", "3HE4", "3HE5", "3HET", "3HEU", "3HEV", "3HEW", "3HEX", "3HEY", "3HEZ", "3HF0", "3KD7", "3L35", "3L36", "3L37", "3LJM", "3LT8", "3LT9", "3LTA", "3LTB", "3LTC", "3LTD", "3M22", "3M24", "3MIP", "3MIS", "3MLG", "3O49", "3O4A", "3O4B", "3O4C", "3O4D", "3OG3", "3OGF", "3OL0", "3P46", "3P6I", "3P6J", "3PBJ", "3PG0", "3PGF", "3Q7W", "3Q7X", "3Q7Y", "3Q9N", "3Q9U", "3QA9", "3QHT", "3R2X", "3R3K", "3R46", "3R47", "3R48", "3R4A", "3R4H", "3RA3", "3RFN", "3RHU", "3RI0", "3RIJ", "3RU8", "3S0R", "3SNV", "3TDM", "3TDN", "3TES", "3TEU", "3TQ2", "3U0S", "3UC7", "3UC8", "3V1A", "3V1B", "3V1C", "3V1D", "3V1E", "3V1F", "3V45", "3V86", "3VB8", "3VDX", "3VJF", "3WW7", "3WW8", "3WW9", "3WWA", "3WWB", "3WWF", "3ZU7", "3ZUV", "4A29", "4AFQ", "4AFS", "4AFU", "4AFZ", "4AG1", "4AG2", "4ATZ", "4CJ0", "4CJ1", "4CJ2", "4D49", "4D4E", "4D8H", "4D9J", "4DAC", "4DB6", "4DB8", "4DB9", "4DBA", "4DRT", "4DUI", "4DZK", "4DZL", "4DZM", "4DZN", "4DZU", "4DZV", "4ESS", "4ETJ", "4F2V", "4G3B", "4G4L", "4G4M", "4GCZ", "4GLA", "4GLU", "4GLV", "4GMR", "4GN3", "4GN4", "4GN5", "4GPM", "4GVV", "4GVW", "4H7R", "4H8F", "4H8G", "4H8L", "4H8M", "4H8O", "4HB5", "4HQD", "4HRL", "4HRM", "4HRN", "4HXT", "4IJB", "4IVH", "4J4A", "4J7W", "4J8Y", "4JB8", "4JMG", "4JMH", "4JW2", "4JW3", "4KGR", "4KGS", "4KGT", "4KVT", "4KVU", "4KVV", "4KY3", "4KYB", "4KYV", "4KYZ", "4LNY", "4LOA", "4LPT", "4LPU", "4LPV", "4LPW", "4LPX", "4LPY", "4LT9", "4M6A", "4N6T", "4N6U", "4NDJ", "4NDK", "4NDL", "4NEY", "4NEZ", "4NTP", "4NTR", "4NW8", "4NW9", "4O5S", "4O5T", "4O60", "4OW4", "4OXW", "4OZA", "4OZB", "4OZC", "4P4V", "4P4W", "4P4X", "4P4Y", "4P4Z", "4P6J", "4P6K", "4P6L", "4PJQ", "4PJR", "4PJS", "4PN8", "4PN9", "4PNA", "4PNB", "4PND", "4PQ8", "4PSJ", "4PWW", "4Q8D", "4QFV", "4QKR", "4QKS", "4QWV", "4R58", "4R5C", "4R5D", "4R6F", "4R6G", "4R6J", "4R80", "4RJV", "4RV1", "4RZP", "4TQL", "4TUT", "4U3H", "4UBY", "4UBZ", "4UOS", "4UOT", "4V3O", "4V3Q", "4V3R", "4W5L", "4W5M", "4W5P", "4W5Y", "4W67", "4W71", "4WBU", "4WBV", "4WN4", "4WPY", "4WSL", "4WSP", "4YDW", "4YDY", "4YFO", "4YXX", "4YXY", "4YXZ", "4YY2", "4YY5", "4Z08", "4ZCN", "4ZN8", "4ZV6", "4ZXZ", "5A0O", "5AEI", "5AWL", "5BOP", "5BVB", "5BVL", "5BYO", "5C39", "5CHB", "5CW9", "5CWB", "5CWC", "5CWD", "5CWF", "5CWG", "5CWH", "5CWI", "5CWJ", "5CWK", "5CWL", "5CWM", "5CWN", "5CWO", "5CWP", "5CWQ", "5CY5", "5D2T", "5D2V", "5D2W", "5D2X", "5D2Y", "5D30", "5D32", "5D33", "5D37", "5D38", "5DI5", "5DN0", "5DNS", "5DQA", "5DRA", "5DXV", "5DZB", "5E5V", "5E5X", "5E5Z", "5E61", "5E6G", "5EHB", "5EIL", "5EOJ", "5EON", "5ET3", "5EZ8", "5EZ9", "5EZA", "5EZC", "5EZE", "5F2Y", "5F53", "5F72", "5GAJ", "5H1H", "5H1I", "5H78", "5H7C", "5HFY", "5HG2", "5HHC", "5HHD", "5HI1", "5HKN", "5HKR", "5HOX", "5HOY", "5HPN", "5HPP", "5HRY", "5HRZ", "5HS0", "5I1N", "5I1O", "5I1P", "5I1S", "5I1Y", "5I1Z", "5IEN", "5IEO", "5IEP", "5IER", "5IF6", "5IZS", "5J0H", "5J0I", "5J0J", "5J0K", "5J0L", "5J10", "5J2L", "5J73", "5J7D", "5JG9", "5JHI", "5JI4", "5JQZ", "5K7V", "5K92", "5KAY", "5KB0", "5KB1", "5KB2", "5KBA", "5KKG", "5KNG", "5KNH", "5KPE", "5KPH", "5KVN", "5KWD", "5KWO", "5KWP", "5KWX", "5KWZ", "5KX0", "5KX1", "5KX2", "5L0P", "5L2H", "5L33", "5LE2", "5LE3", "5LE4", "5LE6", "5LE7", "5LE8", "5LE9", "5LEA", "5LEB", "5LEC", "5LED", "5LEE", "5LEN", "5LW2", "5MFB", "5MFC", "5MFD", "5MFE", "5MFF", "5MFG", "5MFH", "5MFI", "5MFJ", "5MFK", "5MFL", "5MFM", "5MFN", "5MFO", "5SUR", "5SUS", "5SUT", "5SUU", "5T56", "5TPH", "5TPJ", "5TRV", "5TS4", "5TWI", "5TWW", "5U35", "5U59", "5U5A", "5U5B", "5U5C", "5U9T", "5U9U", "5UB0", "5UBS", "5UCE", "5UCF", "5UFE", "5UFQ", "5UHR", "5UN5", "5UN6", "5UOI", "5UP1", "5UP5", "5US3", "5UXT", "5UYO", "5V63", "5V64", "5V65", "5VAV", "5VBT", "5VF1", "5WRX", "5XG5"]
protein_list = []

### Turn PDB into lowercase

for prot in proteins:
    protein_list.append(prot.lower())
textRegex = re.compile(r'\s+')
superfam_dict = {}
domain_dict = {}


### read all lines in pdb and find if they have

all_doms = open('/home/ilya/Projects/De-Novo/data/alldoms.txt', 'r')
for line in all_doms.readlines():
    for protein in protein_list:
        if protein in line:
            print("Now parsing this line:    " + line)
            text_as_list = textRegex.split(line)
            superfam_id = ".".join(text_as_list[1:5])
            superfam_dict[superfam_id] = {}
            domain_dict[text_as_list[0]] = ".".join(text_as_list[1:5])
all_doms.close()

### add empty inputs

for superfam in superfam_dict:
    superfam_dict[superfam] = {
    "domain_list" : [],
    "number_of_all_doms" : 0,
    "number_of_DeNovo_doms" : 0,
    "proportion_of_DeNovo" : 0
    }

### adds all domains to each superfam

for key in domain_dict:
    superfam_dict[domain_dict[key]]["domain_list"].append(key)
all_superfam = open('/home/ilya/Projects/De-Novo/data/allsuperfam.txt', 'r')
all_superfam_dict = {}
for line in all_superfam.readlines():
    print(line)
    text_list = textRegex.split(line)
    all_superfam_dict[text_list[0]] = text_list[2]
pprint(all_superfam_dict)

for superfam in superfam_dict:
    superfam_dict[superfam]["number_of_DeNovo_doms"] = len(superfam_dict[superfam]["domain_list"])
    superfam_dict[superfam]["number_of_all_doms"] = int(all_superfam_dict[superfam])
    superfam_dict[superfam]["proportion_of_DeNovo"] = round(superfam_dict[superfam]["number_of_DeNovo_doms"]/superfam_dict[superfam]["number_of_all_doms"], 3)

### load data as CSV

with open('/home/ilya/Projects/De-Novo/results/final_result.csv', 'w') as finalresult:
    finalresult.write("Superfamily ID,Number of Domains,Number of De-Novo Domains,Proportion of De-Novo\n")
    for key in superfam_dict:
        finalresult.write(key + "," + str(superfam_dict[key]["number_of_all_doms"]) + "," + str(superfam_dict[key]["number_of_DeNovo_doms"]) + "," + str(superfam_dict[key]["proportion_of_DeNovo"]) + "\n")

## save data as JSON

with open('/home/ilya/Projects/De-Novo/results/all_DeNovo.json', 'w') as jsondata:
    json.dump(superfam_dict, jsondata)
pprint(superfam_dict)

with open("/home/ilya/Projects/De-Novo/results/domains.csv", "w") as domaindata:
    domaindata.write("Domain,Superfamily\n")
    for key in domain_dict:
        domaindata.write(key + "," + domain_dict[key] + "\n")
