# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 16:01:47 2019

@author: Raj Tagore
"""

import re
import string
import wordcloud

a = "apuinfqeiupbv verquuvqipruv  epvuin prvn, eqrv6t7623 ;j 6327g6"
a = re.sub(r'\d+', ' ', a)
print(a)
t = str.maketrans('', '', string.punctuation)
a = a.translate(t)
print(a)
a = a.strip()
print(a)