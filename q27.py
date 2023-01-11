# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:38:25 2019

@author: Raj Tagore
"""

from statsmodels.tsa.arima_model import ARIMA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ads.csv')['Ads']
l, t = df.iloc[:170], df.iloc[170:]
model = ARIMA(l, order = (2, 1, 5)).fit()
#order(p, d, q) p =  lag observation
# d = difference value, for eg: 1, 2, 3 or 1, 4, 7.
# q = moving average size = 
p = model.forecast(len(t))
plt.plot(t.index, t)
plt.plot(t.index, p[2])