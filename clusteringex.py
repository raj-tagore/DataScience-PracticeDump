# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:44:25 2019

@author: Mihir
"""
import pandas as pd
import matplotlib.pylab as plt
from sklearn.cluster import KMeans
df=pd.read_csv('iris.csv')
newdf=df.drop('Species',axis=1)
newdf.plot(x='Petal.Length',y='Sepal.Length',kind='scatter')
model.fit(newdf)
model.labels_
model.cluster_centers_
newdf.plot(x='Petal.Length',y='Sepal.Length',c=model.labels_,s=10,kind='scatter',cmap=plt.cm.coolwarm)
newdf['target']=model.labels_
a=[1,2,3,4,5,6,7,8,9,10]
b=[]
for i in range(1,11):
    model=KMeans(n_clusters=i)
    model.fit(newdf)
    b.append(model.inertia_)
plt.plot(a,b)