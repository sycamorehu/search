#!/usr/bin/env python3.7

from bs4 import BeautifulSoup
import urllib3
import requests
import hashlib
import re
import string

# connection pool and request making
http = urllib3.PoolManager()
url = 'http://hotels.ctrip.com/hotel/shanghai2/p4'
response = http.request('GET', url)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(response.data, "html.parser")

# get the whole page
print(soup.prettify())

