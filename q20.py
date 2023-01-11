# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:29:07 2019

@author: Raj Tagore
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score
 

df = pd.read_csv("Classification/weather.csv")
df.replace("NSE", "SE", inplace = True)
df.replace("SSE", "SE", inplace = True)
df.replace("ESE", "SE", inplace = True)
df.replace("WSE", "SE", inplace = True)
df.replace("NSW", "SW", inplace = True)
df.replace("SSW", "SW", inplace = True)
df.replace("ESW", "SW", inplace = True)
df.replace("WSW", "SW", inplace = True)
df.replace("NNE", "NE", inplace = True)
df.replace("SNE", "NE", inplace = True)
df.replace("ENE", "NE", inplace = True)
df.replace("WNE", "NE", inplace = True)
df.replace("NNW", "NW", inplace = True)
df.replace("SNW", "NW", inplace = True)
df.replace("ENW", "NW", inplace = True)
df.replace("WNW", "NW", inplace = True)
df.dropna(inplace = True)

df["WindGustDir"] = df["WindGustDir"].astype("category")
df["WindDir9am"] = df["WindDir9am"].astype("category")
df["WindDir3pm"] = df["WindDir3pm"].astype("category")
df["RainToday"] = df["RainToday"].astype("category")
df["RainTomorrow"] = df["RainTomorrow"].astype("category")


le = LabelEncoder()
df["WindGustDir"] = le.fit_transform(df["WindGustDir"])
df["WindDir9am"] = le.fit_transform(df["WindDir9am"])
df["WindDir3pm"] = le.fit_transform(df["WindDir3pm"])
df["RainToday"] = le.fit_transform(df["RainToday"])
df["RainTomorrow"] = le.fit_transform(df["RainTomorrow"])

dfd = df.drop("RainTomorrow", axis = 1)
xl, xt, yl, yt = train_test_split(dfd, df["RainTomorrow"])

'''
#defining arguments to make a gridSearch model
model = KNeighborsClassifier()
k = list(range(1, 51))
dic = {'n_neighbors' : k}

#defining gridsearch model

gmodel = GridSearchCV(model, dic, cv = 10)
gmodel.fit(xl, yl)
print(gmodel.best_params_)
'''

model = KNeighborsClassifier(n_neighbors = 3)
model.fit(xl, yl)
yp = model.predict(xt)
print(accuracy_score(yp, yt))







