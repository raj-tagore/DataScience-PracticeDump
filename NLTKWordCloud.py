# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 12:21:18 2020

@author: Raj Tagore
"""

import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt

File = open("RandomText.txt", 'r')
stro = File.read()
#CONV TO LOWER
stro = stro.lower()
#remove punctuation
s = str.maketrans("", "", string.punctuation)
stro = stro.translate(s)
#remove excess spaces
stro = stro.strip()
print(stro)
#remove stopwords
st = stopwords.words('english')
wordlist = word_tokenize(stro)

for i in wordlist:
    if i in st:
        wordlist.remove(i)
        
para = ' '.join(wordlist)
        
cloud = WordCloud()
cloud = cloud.generate(para)
plt.imshow(cloud)
#import re
#sentence = ' '.join(re.split("\s", sentence, flags = re.UNICODE))

