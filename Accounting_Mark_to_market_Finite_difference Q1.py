#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Question 1 Task 1A

fv = input("Enter the Face Value: ")
price = input("Enter the Price: ")
n = input("Enter the Number of Years: ")
coupon_payment = 0.05 * 1000

fv = int (fv)
price = int (price)
n = int (n)

def task1 (coupon_payment, fv, price, n):
    ytm = ((coupon_payment + (fv-price)/ n)) / ((fv + price)/2)
    return ytm

print("The YTM for this bond is: " + str(ytm*100) + "% for 1 coupon")


# In[35]:


#Question 1 Task 1B

import math

fv = 1000
price = 1054
n = 10
coupon_payment = 0.05 * 1000

ytm = ((coupon_payment + (fv-price)/ n)) / ((fv + price)/2)

m = 1
c = 0.06
    
bondPrice = ((fv*c/m*(1-(1+ytm/m)**(-m*n)))/(ytm/m)) + fv*(1+(ytm/m))**(-m*n)

print("The YTM for this bond is: " + str(ytm*100) + "% for 1 coupon")

print ("The Bond Price is: " + str (bondPrice))

def error (price, bondPrice):
    function = math.sqrt((price - bondPrice)**2)
    return function

print ("The function result is: " + str(error(price, bondPrice)))


# In[75]:


#Question 1 Task 2

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fv = 1000
price = 1054
n = 25
coupon_payment = 0.05 * 1000

def task1 (coupon_payment, fv, price, n):
    ytm = ((coupon_payment + (fv-price)/ n)) / ((fv + price)/2)
    return ytm

df = pd.DataFrame({
      'x_axis': range(900,1111),
      'y_axis': task1 (coupon_payment, fv, price, n)
  })

# plot
plt.plot('x_axis', 'y_axis', data=df, linestyle='-', marker='o')
plt.show()

df2 = pd.DataFrame({
      'x_axis': range(1,50),
      'y_axis': task1 (coupon_payment, fv, price, n)
  })

# plot
plt.plot('x_axis', 'y_axis', data=df2, linestyle=':', marker='*')
plt.show()


# In[ ]:




