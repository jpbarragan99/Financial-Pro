#!/usr/bin/env python
# coding: utf-8

# In[30]:


#Question 2 Task 1

import pandas as pd
import matplotlib.pyplot as plt

var = pd.read_excel("CORRECTION.xlsx")
print(var)

x = list(var['FORECAST'])
y = list(var['HOUSING1'])

plt.figure(figsize=(10,10))
plt.style.use('seaborn')
plt.scatter(x,y,marker="o",s=100,edgecolors="black",c="red")
plt.title("Housing")
plt.show()


# In[23]:


def variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance

variance(list(var['FORECAST']))


# In[20]:


var2 = pd.read_excel("CORRECTION.xlsx")

x1 = list(var2['FORECASTR'])
y1 = list(var2['FORECAST'])

plt.figure(figsize=(10,10))
plt.style.use('seaborn')
plt.scatter(x1,y1,marker="o",s=100,edgecolors="black",c="blue")
plt.title("Housing")
plt.show()


# In[ ]:




