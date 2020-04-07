#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The aim of this project is to clean the data and analyze the included used car listings.


# In[2]:


import pandas as pd
import numpy as np


# In[3]:


autos = pd.read_csv('autos.csv',encoding = 'Latin-1')


# In[4]:


autos


# In[5]:


print(autos.info())
autos.head()


# In[6]:


autos.columns


# In[7]:


autos.columns = ['date_crawled', 'name', 'seller', 'offer_type', 'price', 'ab_test',
       'vehicle_type', 'registration_year', 'gearbox', 'power_ps', 'model',
       'odometer', 'registration_month', 'fuel_type', 'brand',
       'unrepaired_damage', 'ad_created', 'num_photos', 'postal_code',
       'last_seen']
autos.head()


# In[8]:


autos.describe(include='all')


# In[9]:


autos['price'] = (autos['price'].str.replace(',','')
                             .str.replace('$','')
                             .astype(float)) 
print(autos['price'].head())


# In[10]:


autos['odometer'] = (autos['odometer'].str.replace(',','')
                             .str.replace('km','')
                             .astype(float)) 
print(autos['odometer'].head())


# In[11]:


autos = autos.rename({'odometer':'odometer_km'},axis=1)


# In[12]:


autos["odometer_km"].value_counts()


# In[13]:


autos['price'].value_counts().sort_index(ascending=False).head(20)


# In[14]:


autos = autos[autos['price'].between(1,350001)]
print(autos['price'].describe())


# In[15]:


autos['date_crawled'].value_counts(normalize=True, dropna=False).sort_index()


# In[16]:


autos['date_crawled'].value_counts(normalize=True, dropna=False).sort_values()


# In[17]:


autos['registration_year'].describe()


# In[18]:


autos['registration_year'].value_counts(dropna=False).sort_index()


# In[19]:


autos = autos[autos['registration_year'].between(1900,2016)]
autos['registration_year'].value_counts(normalize=True)


# In[20]:


brandcounts=autos['brand'].value_counts(normalize=True)


# In[21]:


brandcounts = brandcounts[brandcounts > 0.05].index
print(brandcounts)


# In[22]:


mean_price={}
for e in brandcounts:
    mean=autos.loc[autos['brand']==e,'price'].mean()
    mean_price[e]=mean
mean_price


# In[23]:


mean_lineage={}
for l in brandcounts:
    mean=autos.loc[autos['brand']==l,'odometer_km'].mean()
    mean_lineage[l]=mean
mean_lineage


# In[24]:


mean_price_series=pd.Series(mean_price)
mean_price_series


# In[25]:


mean_lineage_series=pd.Series(mean_lineage)
mean_lineage_series


# In[26]:


information=pd.DataFrame(mean_price_series,columns=['Mean price'])
information['Mean mileage']=mean_lineage_series
information

