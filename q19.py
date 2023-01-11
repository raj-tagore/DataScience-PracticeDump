# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:43:17 2019

@author: Raj Tagore
"""

import re
from nltk.tokenize import word_tokenize
import pandas as pd
import string
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv("winemag-data-130k-v2.csv")
df2 = df["description"]
st = ''
st = ''.join(df2)
st = st.lower()

t  = str.maketrans('', '', string.punctuation)
st = st.translate(t)
st = re.sub(r'\d+', '', st)
tok = word_tokenize(st)
sw = set(stopwords.words("english"))
new = []
for word in tok:
    if word not in sw:
        new.append(word)
newst = ''.join(new)
cloud = WordCloud().generate(newst)
plt.imshow(cloud)
