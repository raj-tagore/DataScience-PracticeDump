# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:51:21 2019

@author: Raj Tagore
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt


df = pd.read_csv("Regression_analysis/wbcd.csv")
print(df)
df1=df.drop("id", axis = 1)
print(df1)
dfd = df1.drop("diagnosis", axis = 1)
xl, xt, yl, yt = train_test_split(dfd, df1["diagnosis"])
model = LogisticRegression()
model.fit(xl, yl)
yp = model.predict(xt)
print(confusion_matrix(yt, yp))
print(accuracy_score(yt, yp))

