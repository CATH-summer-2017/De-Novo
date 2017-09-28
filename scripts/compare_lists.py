#!/usr/bin/python3
import re
import csv
from pprint import pprint
superfamRegex = re.compile(r'\w+.\w+.\w+.\w+')
list_of_superfams = []
with open('/home/ilya/Projects/De-Novo/results/superfam_info.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        list_of_superfams.append(row[0])
dict_of_superfams = {}
with open('/home/ilya/Projects/De-Novo/results/all_superfamilies_in_CATH.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        if row[0] in list_of_superfams:
            dict_of_superfams[row[0]] = row[2]
pprint(dict_of_superfams)
