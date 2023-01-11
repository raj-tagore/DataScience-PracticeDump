# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:32:45 2019

@author: Raj Tagore
"""

import pandas as pd
import numpy as np

df = pd.read_csv("insurance.csv")
print(df)
df.replace('[,]', '', regex = True)
print(df[df.Y==0])