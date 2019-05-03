#!/usr/bin/env python
# coding: utf-8

# # Operações
# 
# Há muitas operações com pandas que serão realmente úteis para você, mas não se enquadram em nenhuma categoria distinta. Vamos mostrar aqui nesta aula:

# In[1]:


import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()


# ### Informação sobre valores exclusivos

# In[2]:


df['col2'].unique()


# In[3]:


df['col2'].nunique()


# In[4]:


df['col2'].value_counts()


# ### Selecionando dados

# In[5]:


# Selecione do DataFrame usando critérios de várias colunas
newdf = df[(df['col1']>2) & (df['col2']==444)]


# In[6]:


newdf


# ### Aplicando funções

# In[7]:


def times2(x):
    return x*2


# In[8]:


df['col1'].apply(times2)


# In[9]:


df['col3'].apply(len)


# In[10]:


df['col1'].sum()


# ** Removendo colunas permanentemente **

# In[11]:


del df['col1']


# In[12]:


df


# ** Obter nomes de coluna e índice: **

# In[13]:


df.columns


# In[14]:


df.index


# ** Ordenando um DataFrame **

# In[15]:


df


# In[16]:


df.sort_values(by='col2') #inplace=False por padrão


# ** Encontre Valores Nulos ou Verifique Valores Nulos **

# In[17]:


df.isnull()


# In[18]:


# Deleta linhas com valores NaN
df.dropna()


# ** Preenchendo os valores de NaN com outra coisa: **

# In[19]:


import numpy as np


# In[20]:


df = pd.DataFrame({'col1':[1,2,3,np.nan],
                   'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
df.head()


# In[21]:


df.fillna('Preencher')


# In[22]:


data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)


# In[23]:


df


# In[24]:


df.pivot_table(values='D',index=['A', 'B'],columns=['C'])

