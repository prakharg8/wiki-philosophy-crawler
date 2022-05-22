#!/usr/bin/env python3
import requests
import lxml
from bs4 import BeautifulSoup
from xlwt import *

def visit(url):
    f = requests.get(url)
    soup = BeautifulSoup(f.content, 'lxml')
    print(soup.title.contents[0])
    if url == "https://www.wikipedia.com/wiki/Philosophy":
        return
    ind = 0
    paras = soup.find('div', {'id': 'mw-content-text'}).find_all('p')
    while True:
        if paras[ind].has_attr('class') and paras[ind]['class'] == 'mw-empty-elt' or len(paras[ind].find_all('a')) == 0:
            ind += 1
        else:
            break

    links = paras[ind].find_all('a')
    i = 0
    next_link = links[i]
    while(True):
        if next_link.parent.name == 'p' and next_link['href'].split('-')[0] != "#cite_note" and next_link['href'] != "/wiki/Latin":
            break
        else:
            i += 1
            next_link = links[i]
    new_url = "https://www.wikipedia.com" + next_link['href']
    visit(new_url)

url = "https://www.wikipedia.com/wiki/phone" #+ str(input())
visit(url)
