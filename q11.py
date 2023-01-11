# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:18:01 2019

@author: Raj Tagore
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt


df = pd.read_csv("binary.csv")
xl, xt, yl, yt = train_test_split(df[['rank', 'gre', 'gpa']], df['admit'])
# here xt = x test and xl = x  learn, yp = y predicted
model = LogisticRegression()
model2 = LogisticRegression()
model.fit(xl, yl)
yp = model.predict(xt)
print(confusion_matrix(yt, yp))
print(accuracy_score(yt, yp))
model2.fit(xl[["rank"]], yl)
yp2 = model2.predict(xt[["rank"]])
print(confusion_matrix(yt, yp2))
print(accuracy_score(yt, yp2))
