# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:51:22 2019

@author: Raj Tagore
"""

import re
import string
import wordcloud
from nltk.tokenizeimport word_tokenize


aa = open("FirstYearStats.txt", 'r')
#aa is a file reader
a = aa.read()
#a is a string
print(a)
a = a.lower()
a = re.sub(r'\d+', ' ', a)
print(a)
t = str.maketrans('', '', string.punctuation)
a = a.translate(t)
print(a)
a = a.strip()
print(a)
#a is lowered and cleaned string
#
