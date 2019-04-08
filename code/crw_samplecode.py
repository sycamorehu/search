#!/usr/bin/env python3.7

from bs4 import BeautifulSoup
import urllib3
import requests
import hashlib

# connection pool and request making
http = urllib3.PoolManager()
url = 'http://hotels.ctrip.com/hotel/shanghai2/p1'
response = http.request('GET', url)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(response.data, "html.parser")

# get the whole page
#print(soup.prettify())

# get hotel names
htlname = []
for tag in soup.find_all('h2', class_ = 'hotel_name'):
    htlname.append(tag.text.strip())
print(htlname)

# get hotel ids
htlid = []
hshtlid = []
for tag in soup.find_all('div', class_ = 'hotel_new_list J_HotelListBaseCell'):
    hid = tag.get('id')
    htlid.append(hid)
    hshtlid.append(hashlib.md5(hid.encode()).hexdigest())
print(htlid)
print(hshtlid)

# get hotel_strategymedal
medal = []
qmedal = []
star = []
for ico in soup.find_all('span', attrs = {'class': 'hotel_ico'}):
    #print(ico)
    lmedal = []
    for tag in ico.find_all('span'):
        lmedal.append(tag.attrs['class'])
    if len(lmedal) == 3:
        medal.append(lmedal[0])
        qmedal.append(lmedal[1])
        star.append(lmedal[2])
    if len(lmedal) == 2:
        medal.append(lmedal[0])
        qmedal.append('')
        star.append(lmedal[1])
print('medal list:')
print(medal)
print('qmedal list:')
print(qmedal)
print('star list:')
print(star)

# get hotel picture on the hotel list page
piclink = []
for tag in soup.find_all('div', class_ = 'dpic J_as_bottom'):
    #print(tag.img.get('src'))
    piclink.append(tag.img.get('src'))
print(piclink)

# get hotel address
loc = []
for tag in soup.find_all('p', class_ = 'hotel_item_htladdress'):
    loc.append(tag.text)
print(loc)

# get specials
special = []
for tag in soup.find_all('span', class_ = 'special_label'):
    lspecial = []
    for item in tag.find_all('i'):
        lspecial.append(item.text)
    special.append(lspecial)
print(special)

# get icon list
icon = []
for tag in soup.find_all('div', class_ = 'icon_list'):
    licon = []
    for item in tag.find_all('i'):
        licon.append(item.get('title'))
    icon.append(licon)
print(icon)

# get low price
lowprice = []
for tag in soup.find_all('span', class_ = 'J_price_lowList'):
    lowprice.append(tag.text)
print(lowprice)

# get hotel scores
reclevel = []
reviewscore = []
recpercent = []
reviewnum = []
reccomment = []
for tag in soup.find_all('span', class_ = 'hotel_level'):
    reclevel.append(tag.text)
for tag in soup.find_all('span', class_ = 'hotel_value'):
    reviewscore.append(tag.text)
for tag in soup.find_all('span', class_ = 'total_judgement_score'):
    recpercent.append(tag.span.text)
for tag in soup.find_all('span', class_ = 'hotel_judgement'):
    reviewnum.append(tag.span.text)
for tag in soup.find_all('span', class_ = 'recommend'):
    reccomment.append(tag.text)
print(reclevel)
print(reviewscore)
print(recpercent)
print(reviewnum)
print(reccomment)


for tag in soup.find_all('span', class_ = 'giftcard_available'):
    gcard = []




# name, id, cooperation relationship, star, address, medal list(hotel type),
# facility, review, #reviews, hotel_level, total_judgement_score, recommend_context
