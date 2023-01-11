# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:36:27 2019

@author: Raj Tagore
"""

import numpy as np
import pandas as pd
import seaborn as sb

df2 = pd.read_csv('ads.csv')
#weighted moving avg
df3 = df2[-12:]
wtv = []
for i in range(len(df3)):
    #j = int(df3['Ads'][-(i+1)])/len(df3)*(i+1)
    j = df3.Ads.iloc[-i-1]*((i+1)/len(df3))
    wtv.append(j)
print(np.average(wtv))
print(np.average())
