#!/usr/bin/env python
# coding: utf-8

# # Groupby
# 
# O método groupby permite agrupar linhas de dados em conjunto e chamar funções agregadas

# In[6]:


import pandas as pd
# Cria um DataFrame
data = {'Empresa':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Nome':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Venda':[200,120,340,124,243,350]}


# In[7]:


df = pd.DataFrame(data)


# In[8]:


df


# ** Agora, você pode usar o método .group by () para agrupar as linhas em conjunto com base em um nome de coluna. Por exemplo, vamos agrupar com base na empresa. Isso criará um objeto DataFrameGroupBy:**

# In[12]:


df.groupby('Empresa')


# Você pode salvar este objeto como uma nova variável:

# In[13]:


por_companhia = df.groupby("Empresa")


# E, em seguida, chamar métodos agregados do objeto:

# In[14]:


por_companhia.mean()


# In[17]:


df.groupby('Empresa').mean()


# Mais exemplos de métodos agregados:

# In[18]:


por_companhia.std()


# In[19]:


por_companhia.min()


# In[20]:


por_companhia.max()


# In[21]:


por_companhia.count()


# In[22]:


por_companhia.describe()


# In[23]:


por_companhia.describe().transpose()


# In[24]:


por_companhia.describe().transpose()['GOOG']

