#!/usr/bin/env python3.7

from bs4 import BeautifulSoup
from time import sleep
from random import randint
import urllib3
import requests
import string

hotel_name = []
hotel_id = []

# connection pool and request making
http = urllib3.PoolManager()
for i in range(1,11):
    url = 'http://hotels.ctrip.com/hotel/shanghai2/p'
    url += str(i)
    sleep(randint(1,4))
    print(url)

    response = http.request('GET', url)

    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(response.data, "html.parser")

    # get the whole page
    #print(soup.prettify())

    # get hotel names
    for htl in soup.find_all('h2', class_ = 'hotel_name'):
        hotel_name.append(htl.text.strip())
    print(hotel_name)

    # get hotel ids
    for tag in soup.find_all('div', class_ = 'hotel_new_list J_HotelListBaseCell'):
        hotel_id.append(tag.get('id'))
    print(hotel_id)

for j in range(len(hotel_name)):
    print('{0:10} {}!'.format(hotel_name[j], hotel_id[j]))
