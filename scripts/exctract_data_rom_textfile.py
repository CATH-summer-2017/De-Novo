#!/usr/bin/python3
import csv
import re
from pprint import pprint
txt_file = open("/home/ilya/Projects/De-Novo/results/all_superfamilies.txt", 'r')
csv_file = open("/home/ilya/Projects/De-Novo/results/all_CATH_superfam.csv", 'w')
filetags = ["Superfamily", "S35", "Total Domains", "Description"]
w = csv.writer(csv_file, filetags)
w.writerow(filetags)
lines_list = txt_file.readlines()
textRegex = re.compile(r'\s\s+')
for line in lines_list:
    w.writerow(textRegex.split(line))
