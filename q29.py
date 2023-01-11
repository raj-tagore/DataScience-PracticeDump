# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 15:12:05 2019

@author: Raj Tagore
"""

import numpy as np
from statistics import mode
import scipy.stats as sc
import matplotlib.pyplot as plt

arr = np.random.randint(0, 100, 50, dtype = 'int8')
r = np.arange(0, 50)

print(np.mean(arr))
print(np.median(arr))
print(np.var(arr))
print(np.std(arr))
print(np.max(arr))
print(np.min(arr))
z = sc.norm.ppf(q = 0.95)
t = sc.t.ppf(q = 0.95, df = 49)
#for z
print("for z:")
MOE = z*np.std(arr)/np.sqrt(len(arr))
print("moe is: ", MOE)
print('Upper boundary: ', MOE + np.mean(arr))
print('lower boundary: ', MOE - np.mean(arr))
print("for t:")
MOE = t*np.std(arr)/np.sqrt(len(arr))
print("moe is: ", MOE)
print('Upper boundary: ', MOE + np.mean(arr))
print('lower boundary: ', MOE - np.mean(arr))
plt.plot(r, arr)
print(sc.kurtosis(arr))
print(sc.skew(arr))


'''
to find confidence level, 
confidence interval = measure of error +- sample mean
measure of error = critical value probability (z or t) * std/sqrt(size)
alpha = 1-(Confidence Level/100)
critical value probability = 1-(alpha/2)
critical value probability =
                 z = sc.norm.ppf(q = 0.95)
                 t = sc.norm.ppf(q = 0.95)
From CL = 95% get alpha
from alpha get CVP
from CVP get z and t
these are CVP
from CVP get MOE
from MOE get CI
from MOE get upp boundary and low boundary
'''
