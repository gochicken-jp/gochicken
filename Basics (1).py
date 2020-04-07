#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
recent_grads = pd.read_csv('recent-grads.csv')
print(recent_grads.iloc[0])
print(recent_grads.head())
print(recent_grads.tail())


# In[2]:


raw_data_count = len(recent_grads)
recent_grads = recent_grads.dropna()
cleaned_data_count = len(recent_grads)
print(raw_data_count)
print(cleaned_data_count)


# In[3]:


recent_grads.plot(x='Sample_size', y='Median', kind='scatter')


# In[4]:


recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')


# In[5]:


recent_grads.plot(x='Full_time', y='Median', kind='scatter')


# In[6]:


recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter')


# In[7]:


recent_grads.plot(x='Men', y='Median', kind='scatter')


# In[8]:


recent_grads.plot(x='Women', y='Median', kind='scatter')


# In[18]:


cols = ['Sample_size','Median','Employed','Full_time','ShareWomen','Unemployment_rate','Men','Women']
fig = plt.figure(figsize=(5,12))
for r in range(1,5):
    ax = fig.add_subplot(4,1,r)
    ax = recent_grads[cols[r]].plot(kind='hist', rot=40)


# In[20]:


from pandas.plotting import scatter_matrix
scatter_matrix(recent_grads[['Sample_size','Median']])


# In[21]:


scatter_matrix(recent_grads[['Sample_size','Median','Unemployment_rate']])


# In[22]:


recent_grads[:10].plot.bar(x='Major', y='ShareWomen')
recent_grads[163:].plot.bar(x='Major', y='ShareWomen')


# In[ ]:




