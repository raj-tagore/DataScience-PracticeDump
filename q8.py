# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:57:05 2019

@author: Raj Tagore
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


df = pd.read_csv("P4-Demographic-Data.csv")
print(df)
print(df.corr())
mod = LinearRegression()
mod.fit(df[["Birth rate"]], df["Internet users"])
prediction = mod.predict(df[["Birth rate"]])
plt.scatter(df["Birth rate"], df["Internet users"])
plt.scatter(df["Birth rate"], prediction)