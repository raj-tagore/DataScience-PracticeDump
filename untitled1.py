# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 12:53:06 2020

@author: Raj Tagore
"""


import requests
from bs4 import BeautifulSoup
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

TotalNames = []
TotalAbouts = []
TotalPrices = []
for i in range(22):
    url = "https://www.flipkart.com/search?q=samsung+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=samsung+mobiles%7CMobiles&requestId=ba996210-35c7-46e9-b3a4-2cc4a4e99d67&as-searchtext=samsun&page="+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html5lib")
    PageNames = soup.findAll("div", attrs={"class", "_3wU53n"})
    TotalNames.append(PageNames)
    PageAbouts = soup.findAll("div", attrs={"class", "_3ULzGw"})
    TotalAbouts.append(PageAbouts)
    PagePrices = soup.findAll("div", attrs={"class", "1vC4OE_2rQ-NK"})
    TotalPrices.append(PagePrices)
a = {'Names':TotalNames, 'ABouts':TotalAbouts, 'Prices':TotalPrices}
df = pd.DataFrame(a)
    
   