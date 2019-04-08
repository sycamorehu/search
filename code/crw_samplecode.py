#!/usr/bin/env python3.7

from bs4 import BeautifulSoup
from time import sleep
from random import randint
import urllib3
import requests
import hashlib
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-o',
    help = 'output file'
    )
args = vars(parser.parse_args())


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
    htlname = []
    for tag in soup.find_all('h2', class_ = 'hotel_name'):
        htlname.append(tag.text.strip())
    htlname2 = []
    p = re.compile('"name":"(.*?)"')
    htlname2.extend(p.findall(str(soup)))

# get hotel ids
    htlid = []
    hshtlid = []
    for tag in soup.find_all('div', class_ = 'hotel_new_list J_HotelListBaseCell'):
        hid = tag.get('id')
        htlid.append(hid)
        hshtlid.append(hashlib.md5(hid.encode()).hexdigest())
    htlid2 = []
    p = re.compile('"id":"([0-9]*?)"')
    htlid2.extend(p.findall(str(soup))[7:])

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

# get hotel picture on the hotel list page
    imglink = []
    for tag in soup.find_all('div', class_ = 'dpic J_as_bottom'):
        imglink.append(tag.img.get('src'))

# get hotel address
    loc = []
    for tag in soup.find_all('p', class_ = 'hotel_item_htladdress'):
        loc.append(tag.text)

# get specials
    special = []
    for tag in soup.find_all('span', class_ = 'special_label'):
        lspecial = []
        for item in tag.find_all('i'):
            lspecial.append(item.text)
        special.append(lspecial)

# get icon list
    icon = []
    for tag in soup.find_all('div', class_ = 'icon_list'):
        licon = []
        for item in tag.find_all('i'):
            licon.append(item.get('title'))
        icon.append(licon)

# get low price
    lowprice = []
    for tag in soup.find_all('span', class_ = 'J_price_lowList'):
        lowprice.append(tag.text)

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
    revscore = []
    revcount = []
    recscore = []
    p = re.compile('"score":"([0-9]*\.[0-9]*)"')
    revscore.extend(p.findall(str(soup)))
    p = re.compile('"dpscore":"([0-9]*)"')
    recscore.extend(p.findall(str(soup)))
    p = re.compile('"dpcount":"([0-9]*)"')
    revcount.extend(p.findall(str(soup)))


# get latitude and longitude
    lat = []
    p = re.compile('"lat":"([0-9]*\.[0-9]*)"')
    lat.extend(p.findall(str(soup)))

    lon = []
    p = re.compile('"lon":"([0-9]*\.[0-9]*)"')
    lon.extend(p.findall(str(soup)))


    f = open('%s' % args['o'], 'a')
    for i in range(len(htlid)):
        f.write('%s\t' % htlid[i])
        f.write('%s\t' % htlname[i])
        #f.write('%s\t' % htlname2[i])
        f.write('%s\t' % hshtlid[i])
        f.write('%s\t' % medal[i])
        f.write('%s\t' % qmedal[i])
        f.write('%s\t' % star[i])
        f.write('%s\t' % reclevel[i])
        f.write('%f\t' % float(reviewscore[i]))
        f.write('%s\t' % recpercent[i])
        f.write('%d\t' % int(reviewnum[i]))
        f.write('%d\t' % int(lowprice[i]))
        f.write('%s\t' % reccomment[i])
        f.write('%s\t' % special[i])
        f.write('%s\t' % icon[i])
        f.write('%s\t' % loc[i])
        f.write('%s\n' % imglink[i])
    f.close()
