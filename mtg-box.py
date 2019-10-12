# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 18:11:35 2019

@author: cohen
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

cn = input("Card name?")
while(cn != "Exit"):
    cn = cn.replace(" ","+")
    resp = requests.get("https://api.scryfall.com/cards/named?fuzzy="+cn)
        if resp.status_code == 200:
            data = resp.json()
            setname = data['set_name']
            setname = setname.replace(" ","+")
            url = "https://www.mtggoldfish.com/price/"+setname+"/"+cn+"#paper"
            content = urlopen(url)
            soup = BeautifulSoup(content.read())
            played = soup.find_all(class_="col-num-decks")
            sum = 0
            for p in len(played):
                sum += int(played[p].string)
            #Now we have total popularity number
            
        else:
            print("Something went wrong");