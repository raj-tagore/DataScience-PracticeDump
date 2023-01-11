# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:47:34 2019

@author: Raj Tagore
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("US_births_2000-2014_SSA(1).csv")
print(df)
df1 = df.groupby('year').sum()
print(df1.corr())