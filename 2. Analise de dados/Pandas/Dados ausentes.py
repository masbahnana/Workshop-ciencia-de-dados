#!/usr/bin/env python
# coding: utf-8

# # Dados ausentes
# 
# Vamos mostrar alguns métodos convenientes para lidar com Missing Data em pandas:

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})


# In[3]:


df


# In[4]:


df.dropna()


# In[5]:


df.dropna(axis=1)


# In[6]:


df.dropna(thresh=2)


# In[7]:


df.fillna(value='Conteúdo')


# In[8]:


df['A'].fillna(value=df['A'].mean())

