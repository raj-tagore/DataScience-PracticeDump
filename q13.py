# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:32:26 2019

@author: Raj Tagore
"""

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score


var = load_digits()
dir(var)
#selection of model, and giving it to a variable
model = LogisticRegression()
#dividiing our data into learn and test
xl, xt, yl, yt = train_test_split(var["data"], var["target"])
#teaching our model
model.fit(xl, yl)
#predicting new data and giving it to yp = y-predicted
yp = model.predict(xt)
#checking if our model works by seeing predicted values vs actual
print(confusion_matrix(yt, yp))
print(accuracy_score(yt, yp))