# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:36:34 2019

@author: Raj Tagore
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("areavspricedata.csv")
df.corr()
model = LinearRegression()
model.fit(df[['area']], df['price'])
prediction = model.predict(df[['area']])
plt.plot(df['area'], df['price'])
plt.plot(df['area'], prediction)