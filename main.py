import numpy as numpy #linear algebra
import pandas as pd #data processing
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv("./pokemon.csv")
# print(data.info())

#correlation map
f,ax = plt.subplots(figsize=(18, 18))
print(sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax))
