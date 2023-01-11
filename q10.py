# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:40:44 2019

@author: Raj Tagore
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 1000, 1)
y = 1/(2.73**x)
plt.plot(x, y)