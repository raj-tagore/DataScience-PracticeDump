# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 16:38:30 2019

@author: Raj Tagore
"""

import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt

df = pd.read_csv('ads.csv')['Ads']
l, t = df.iloc[:170], df.iloc[170:]
model = ExponentialSmoothing(l, seasonal = 'mul', 
                             seasonal_periods = 24).fit()
y = np.arange(46)
p = model.forecast(len(t))
plt.plot(t.index, t)
plt.plot(y+170, p)
