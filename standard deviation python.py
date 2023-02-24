#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


path="D:\IBM-313 Marks.xlsx"
show=pd.read_excel(path)
print(show)


# In[3]:


a = show["Total"]
np.mean(a)


# In[4]:


np.median(a)


# In[5]:


import scipy 
from scipy import stats
stats.mode


# In[6]:


np.var(a)


# In[7]:


import statistics
statistics.pstdev(a)


# In[8]:


statistics.stdev(a)


# In[9]:


from scipy.stats import skew
skew(a)


# In[12]:


from matplotlib import pyplot as plt
plt.boxplot(a,sym="*")


# In[ ]:




