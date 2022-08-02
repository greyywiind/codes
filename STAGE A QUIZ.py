#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
food_data= pd.read_csv("food_balance.csv", encoding='latin-1')
food_data.describe(include='all')


# In[71]:


food_data.groupby('Item')['Item'].count()


# In[29]:


food_data.isnull().sum()


# In[69]:


food_data.groupby('Item')['Item'].count()


# In[52]:


food_data.groupby('Element').count()


# In[77]:


food_data.groupby(['Area','Element','Item']).count()


# In[ ]:


food_data.groupby('Item')['Item'].count()

