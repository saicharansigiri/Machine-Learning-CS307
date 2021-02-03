#!/usr/bin/env python
# coding: utf-8

# For a given dataset: (1,1.2), (2,1.9), (3,3.2)
# Find the line which fits the data using maximum likelihood function. Plot the line with the given dataset
# Please take beta = 1; therefore you need to find only w (i.e. intercept and slope only).

# In[5]:


import numpy as np
import matplotlib.pyplot as plt


# In[20]:


def simple_linear_regression(x, y):
    n = len(x)
    
    x_mean = sum(x)/n
    y_mean = sum(y)/n
    
    slope_n = 0
    slope_d = 0
    
    for i in range(n):
        slope_n += x[i]*y[i] - y_mean*x[i]
        slope_d += x[i]**2 - x[i]*x_mean
        slope = slope_n/slope_d
        intercept = y_mean - slope*x_mean
        
        return slope,intercept


# In[21]:


x = np.array([1, 2, 3])
y = np.array([1.2, 1.9, 3.2])


# In[22]:


m, c = simple_linear_regression(x, y)


# In[34]:


plt.plot(x, m*x + c)
plt.plot(x, y, 'ro')
plt.title("Best fit line")
plt.xlabel("X")
plt.ylabel("Y")


# In[ ]:




