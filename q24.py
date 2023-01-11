# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:04:29 2019

@author: Raj Tagore
"""

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv("shampoo.csv", 
                 index_col = ['Month'], 
                 parse_dates = ['Month'])
plt.bar(df.index.values, df['Sales'])
plt.xticks(rotation = 90)
v = []
v.append(np.average(df[-12:]))
