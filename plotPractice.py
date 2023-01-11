# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:35:17 2019

@author: Raj Tagore
"""

import pandas as pd
import matplotlib.pyplot as plt

dat = pd.read_csv("drinks.csv")
dat1 = dat[["country","beer_servings"]].nlargest(5, "beer_servings")
print(dat1)
plt.bar(dat1['country'], dat1['beer_servings'])
dat2 = dat.nlargest(5, "spirit_servings")
print(dat2)
plt.bar(dat1['country'], dat1['spirit_servings'])
dat3 = dat.nlargest(5, "wine_servings")
print(dat3[["country", "wine_servings"]])
plt.bar(dat1['country'], dat1['wine_servings'])


df = pd.read_csv(".csv")
