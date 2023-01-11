# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:19:48 2019

@author: Raj Tagore
"""
import pandas as pd
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt


df = pd.read_csv("areavspricedata.csv")
print(df.corr())
plt.scatter(df["area"], df["price"])
m=LinearRegression()
m.fit(df[["area"]], df["price"])
print(m.predict([[3300]]))
print(m.predict([[5000]]))