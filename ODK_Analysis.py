#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file = pd.read_csv('PriceSurveillanceFormSoybean_v1.0.0 (3).csv')


# In[2]:


print(file.head())
print(file.columns)
from datetime import datetime
a = pd.to_datetime(file['start'])
day=[]
for i in a:
    day.append(i.strftime('%A'))
file['Day']=day


# In[3]:


print(file['intro.odk-crop.name'].unique())
print(file['intro.odk-moisture.level_ID'].unique())
print(file['intro.odk-CROP_QUALITY_ID'].unique())
print(file['intro.odk-trade.type'].unique())
print(file['intro.odk-mandi.name'].unique())
cols=['intro.odk-crop.name','intro.odk-moisture.level_ID','intro.odk-CROP_QUALITY_ID','intro.odk-trade.type','intro.odk-mandi.name','Day','intro.odk-data.entry']


# In[4]:


for i in cols:
    print(file.groupby(i)['intro.odk-rate_ID'].mean())


# In[5]:


print(file['intro.odk-trader.name'].value_counts())
print(file['intro.odk-entry.name'].value_counts())
print(file['Day'].value_counts())
print(file['intro.odk-mandi.name'].value_counts())
print(file['intro.odk-CROP_QUALITY_ID'].value_counts())

print(file['intro.odk-trade.type'].value_counts())


# In[6]:


print((file['intro.odk-entry.name'].value_counts()))


# In[7]:


price_type=file[['today','intro.odk-trade.type','intro.odk-rate_ID']]
print(price_type.head())


# In[8]:


type1 = price_type[price_type['intro.odk-trade.type']==1]
type2 = price_type[price_type['intro.odk-trade.type']==2]
type1.columns=['Date','Trade_type','Local Trader Price']
type2.columns=['Date','Trade_type','Market Yard Price']


# In[9]:


merged_price = type1.merge(type2, on='Date',how='outer')


# In[25]:


a=pd.DataFrame((file['today'].value_counts())).reset_index()
b=pd.DataFrame(file.groupby('today')['intro.odk-rate_ID'].mean()).reset_index()


# In[27]:


a.columns=['Date','Entries']
b.columns=['Date','Average Price']
print(a.head())
print(b.head())


# In[28]:


merge_corr = a.merge(b,on='Date',how='outer')


# In[31]:


print(merge_corr)
merge_corr.to_excel('merge_corr.xlsx')

