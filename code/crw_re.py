#!/usr/bin/env python3.7

from bs4 import BeautifulSoup
import urllib3
import requests
import hashlib
import re
import string

# connection pool and request making
http = urllib3.PoolManager()
url = 'http://hotels.ctrip.com/hotel/shanghai2/p2'
response = http.request('GET', url)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(response.data, "html.parser")

# get the whole page
#print(soup.prettify())


p = re.compile('"id":"([0-9]*)"')
data = p.findall(str(soup))
print(data[7:])

p = re.compile('"name":"(.*?)"') # ? to match until the first "
data = p.findall(str(soup))
print(data)

# lat, lon
p = re.compile('"lat":"([0-9]*\.[0-9]*)"')
data = p.findall(str(soup))
print(data)

p = re.compile('"lon":"([0-9]*\.[0-9]*)"')
data = p.findall(str(soup))
print(data)

p = re.compile('"score":"([0-9]*\.[0-9]*)"')
data = p.findall(str(soup))
print(data)

p = re.compile('"dpscore":"([0-9]*)"')
data = p.findall(str(soup))
print(data)

p = re.compile('"dpcount":"([0-9]*)"')
data = p.findall(str(soup))
print(data)



# recommend
recom = []
for tag in soup.find_all('div', class_ = 'hotelitem_judge_box'):
    # print(tag)
    item = tag.find('span', class_ = 'recommend')
    if item:
        recom.append(item.text)
    else:
        recom.append('null')
print(recom)
