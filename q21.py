# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 15:10:53 2019

@author: Raj Tagore
"""

from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus

df = pd.read_csv("Regression_analysis/diabetes.csv")
dfd = df.drop("Outcome", axis = 1)
xl, xt, yl, yt = train_test_split(dfd, df["Outcome"])
model = DecisionTreeClassifier()
model.fit(xl, yl)
yp = model.predict(xt)
print(accuracy_score(yp, yt))
cols = dfd.columns

IOvar = StringIO()
export_graphviz(model, out_file = IOvar, filled = True, 
                special_characters = True,
                feature_names = cols, 
                class_names = ['0', '1'])
graph = pydotplus.graph_from_dot_data(IOvar.getvalue())
graph.write_png('tree1.png')
Image(graph.create_png())

