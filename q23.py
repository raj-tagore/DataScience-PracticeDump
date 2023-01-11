# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 16:58:58 2019

@author: Raj Tagore
"""

from sklearn.tree import export_graphviz
from sklearn.ensemble import RandomForestClassifier 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus

df = pd.read_csv("CTG.csv")
dfd = df.drop("NSP", axis = 1)
xl, xt, yl, yt = train_test_split(dfd, df["NSP"])
model = RandomForestClassifier()
model.fit(xl, yl)
yp = model.predict(xt)
print(accuracy_score(yp, yt))


