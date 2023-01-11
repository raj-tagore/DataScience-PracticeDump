# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:44:27 2019

@author: Raj Tagore
"""

import pandas as pd
import numpy as np

df = pd.read_csv("P4-Demographic-Data.csv")
print(df)
data = df.groupby(["Income Group"])['Birth rate'].max()
for i in range(4):
    print(df[df["Birth rate"]==data[i]])
