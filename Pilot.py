import pandas as pd
import numpy as np

c = {"temperature":["32F", "26C", 9999, 0], "speed":["256mph", "344mph", 9999, "4444kmh"], "weather":["Rainy", "Cloudy", "9999", "166"]}
l = pd.DataFrame(c)
m = l.iloc[1:3, 1:3]
print(l)
print(l.shape)
print(l.describe())
l.replace("32F", 32)
l.replace("[A-Za-z]", "", regex=True, inplace=True)
l.replace({'temperature':9999, 'weather':['9999', '166']}, 0, regex=True, inplace=True)
print(l)
print(l.dtypes)
l["temperature"] = l["temperature"].astype("int")
l["speed"] = l["speed"].astype("int")
print(l.dtypes)