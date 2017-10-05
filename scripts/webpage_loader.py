#!/usr/bin/python3
import requests
from pprint import pprint

u_a = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
def get_page():
    res = requests.get("http://download.cathdb.info/cath/releases/latest-release/cath-classification-data/cath-domain-list.txt", headers={"USER-AGENT":u_a})
    return res.text
txt_file = open("/home/ilya/Projects/De-Novo/data/alldoms.txt", "w")
txt_file.write(get_page())
