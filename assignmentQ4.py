# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 16:22:29 2019

@author: Raj Tagore
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("P4-Demographic-Data.csv")
plt.pie(df.groupby("Income Group").size(), autopct = "%0.0f%%")
print(df.corr())
