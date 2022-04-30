#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

gspc_df = yf.download('^GSPC', 
                      start='2002-01-02', 
                      end='2019-12-31', 
                      progress=False,
)
gspc_df.head()

print (gspc_df)

ticker = yf.Ticker('^GSPC')
gspc_df = ticker.history(period="17y")
gspc_df['Close'].plot(title="S&P 500")


# In[3]:


#Question 3 Task 1.1

# import module
from tabulate import tabulate
 
#create data
data = [["AAAA","1%","10%" , "9%", "37%", -0.08, 2], 
        ["BBBB","0%","14%" , "12%", "20%", -0.86, 2], 
        ["CCCC","1%","8%" , "10%", "20%", -1.13, 1], 
        ["DDDD","2%","15%" , "9%", "37%", -0.47, 1]]
  
#define header names
col_names = ["Symbol", "Average Return", "Volatility", "Risk Free Rate",  "Beta CAPM",  "Sharpe Ratio",  "Average Number of Firms"]
  
#display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))


# In[4]:


#Question 3 Task 1.2

# import module
from tabulate import tabulate
 
#create data
data = [["EWST",11.3 ,3401000000 , "96%", 10.82], 
        ["EGAS",8.6 ,150583000 , "4%", 0.36],]
  
#define header names
col_names = ["Symbol", "Price", "Market Cap", "Weight",  "Weighted Price"]
  
#display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))


# In[5]:


#Question 3 Task 1.2

# import module
from tabulate import tabulate
 
#create data
data = [["SABC",11.8 ,88300000 , "62%", 7.35], 
        ["BTFG",12.15 ,53540000 , "38%", 4.59],]
  
#define header names
col_names = ["Symbol", "Price", "Market Cap", "Weight",  "Weighted Price"]
  
#display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))


# In[6]:


#Question 3 Task 1.2

# import module
from tabulate import tabulate
 
#create data
data = [["JJSF",19.12 ,2914000000 , "100%", 19.12],]
  
#define header names
col_names = ["Symbol", "Price", "Market Cap", "Weight",  "Weighted Price"]
  
#display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))


# In[7]:


#Question 3 Task 1.2

# import module
from tabulate import tabulate
 
#create data
data = [["AEPI",31.62 ,48659000000 , "100%", 31.62],]
  
#define header names
col_names = ["Symbol", "Price", "Market Cap", "Weight",  "Weighted Price"]
  
#display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))


# In[8]:


#Question 3 Task 2A

import pandas as pd
import matplotlib.pyplot as plt

var = pd.read_excel("Q3CORRECTION.xlsx", sheet_name="PORT1")

x = list(var['date'])
y = list(var['Cumulative Returns'])

plt.plot(x, y)
plt.title('PORTFOLIO 1')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.show()


# In[9]:


#Question 3 Task 2B

import pandas as pd
import matplotlib.pyplot as plt

var = pd.read_excel("Q3CORRECTION.xlsx", sheet_name="PORT2")

x = list(var['date'])
y = list(var['Cumulative Returns'])

plt.plot(x, y)
plt.title('PORTFOLIO 2')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.show()


# In[10]:


#Question 3 Task 2C

import pandas as pd
import matplotlib.pyplot as plt

var = pd.read_excel("Q3CORRECTION.xlsx", sheet_name="PORT3")

x = list(var['date'])
y = list(var['Cumulative Returns'])

plt.plot(x, y)
plt.title('PORTFOLIO 3')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.show()


# In[11]:


#Question 3 Task 2D

import pandas as pd
import matplotlib.pyplot as plt

var = pd.read_excel("Q3CORRECTION.xlsx", sheet_name="PORT4")

x = list(var['date'])
y = list(var['Cumulative Returns'])

plt.plot(x, y)
plt.title('PORTFOLIO 4')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.show()


# In[15]:


#Question 3 Task 3

var = pd.read_excel("Q3CORRECTION.xlsx", sheet_name="PORT1")

x = list(var['date'])
y = list(var['Cumulative Returns 3'])

plt.plot(x, y)
plt.title('PORTFOLIO 1')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.show()

var1 = pd.read_excel("Q3CORRECTION.xlsx", sheet_name="PORT3")

x1 = list(var1['date'])
y1 = list(var1['Cumulative Returns 3'])

plt.plot(x1, y1)
plt.title('PORTFOLIO 2')
plt.xlabel('date')
plt.ylabel('Cumulative Returns')
plt.show()

var2 = pd.read_excel("Q3CORRECTION.xlsx", sheet_name="PORT4")

x2 = list(var2['date'])
y2 = list(var2['Cumulative Returns 3'])

plt.plot(x2, y2)
plt.title('PORTFOLIO 3')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.show()

print("For portfolio 1 the total gain is, 1951.951, and the average annual return is, 212.663")
print("For portfolio 2 the total gain is, 2429.411, and the average annual return is, 252.450")
print("For portfolio 3 the total gain is, 3046.83, and the average annual return is, 303.903")


# In[ ]:




