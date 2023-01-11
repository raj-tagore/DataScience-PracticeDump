import pandas as pd 
from sklearn.linear_model import LinearRegression
import numpy as np 
df = pd.read_csv("areavspricedata.csv")
print(df.corr())