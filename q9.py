# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:09:09 2019

@author: Raj Tagore
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


df = pd.read_csv("Advertising.csv")
print(df)
print(df.corr())
mod = LinearRegression()
mod.fit(df[["TV", "Radio"]], df["Sales"])
prediction = mod.predict(df[["TV", "Radio"]])
plt.scatter(df["TV"], df["Sales"])
plt.scatter(df["TV"], prediction)