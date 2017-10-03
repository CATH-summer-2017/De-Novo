#!/usr/bin/python3
import csv
from pprint import pprint
emptydict = {}
with open('/home/ilya/Projects/De-Novo/results/pdb_superfam.csv', 'r') as origfile:
    reader = csv.reader(origfile)
    for row in reader:
        newlist = []
        if row[1] not in emptydict:
            newlist.append(row[0])
            emptydict[row[1]] = newlist
        else:
            newlist = emptydict[row[1]]
            newlist.append(row[0])
            emptydict[row[1]] = newlist
pprint(emptydict)
tempcount = open('/home/ilya/Projects/De-Novo/tempcount.csv', 'w')
for key in emptydict:
    tempcount.write(key + "," + str(len(emptydict[key])) + "\n")
