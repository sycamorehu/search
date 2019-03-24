#!/usr/bin/env python3.7

from bs4 import BeautifulSoup
import urllib3
import requests

# connection pool and request making
http = urllib3.PoolManager()
url = 'http://hotels.ctrip.com/hotel/shanghai2/p1'
response = http.request('GET', url)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(response.data, "html.parser")

# get the whole page
#print(soup.prettify())

# get hotel names
hotel_name = []
for htl in soup.find_all('h2', class_ = 'hotel_name'):
    #print htl.text.strip()
    hotel_name.append(htl.text.strip())
print(hotel_name)

# get hotel ids
hotel_id = []
for tag in soup.find_all('div', class_ = 'hotel_new_list J_HotelListBaseCell'):
    hotel_id.append(tag.get('id'))
print(hotel_id)

# name, id, cooperation relationship, star, address, medal list(hotel type),
# facility, review, #reviews, hotel_level, total_judgement_score, recommend_context