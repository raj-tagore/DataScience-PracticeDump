# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 16:16:34 2019000

@author: Raj Tagore
"""

import numpy as np
import scipy.stats as sc
import seaborn as sns
from scipy.stats import norm, binom, poisson

ndat = norm.rvs(size = 1000, scale = 2, loc = 0)
bdat = binom.rvs(size = 1000, n = 20, p = 0.2)
pdat = poisson.rvs(mu = 2, size = 1000)
sns.distplot(ndat)
sns.distplot(bdat)
sns.distplot(pdat)
