# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:49:36 2020

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



totalReviews = []
for i in range(10):
    url = "https://www.flipkart.com/motorola-g8-power-lite-royal-blue-64-gb/product-reviews/itm8a408329ff3d2?pid=MOBFZ5EXNSGJJ2ZR&lid=LSTMOBFZ5EXNSGJJ2ZRBFFMHB&marketplace=FLIPKART&page="+str(2)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html5lib")
    AllReviews = soup.findAll("div", attrs={"class", "qwjRop"})
    AllReviewsString = []
    for j in AllReviews:
        AllReviewsString.append(j.text)
    totalReviews.append(AllReviewsString)
for i in totalReviews:    
    stro = ' '.join(i)

stro = stro.lower()
#remove punctuation
s = str.maketrans("", "", string.punctuation)
stro = stro.translate(s)
#remove excess spaces
stro = stro.strip()
print(stro)
#remove stopwords
st = stopwords.words('english')
st.append('the')
wordlist = word_tokenize(stro)

for i in wordlist:
    if i in st:
        wordlist.remove(i)
        
para = ' '.join(wordlist)
        
cloud = WordCloud()
cloud = cloud.generate(para)
 plt.imshow(cloud)