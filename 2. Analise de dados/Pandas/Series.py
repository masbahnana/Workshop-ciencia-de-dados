#!/usr/bin/env python
# coding: utf-8

# # Series
# 
# O primeiro tipo de dado que aprenderemos é a Serie. Vamos importar Pandas e explorar tal objeto.
# 
# A Serie é muito semelhante a uma matriz NumPy (na verdade, ela é construída em cima do objeto de matriz NumPy). O que diferencia a matriz NumPy de uma Série, é que uma Serie pode ter rótulos de eixos, o que significa que pode ser indexado por um rótulo, em vez de apenas uma localização numérica. Também não precisa manter dados numéricos, ele pode conter qualquer objeto Python arbitrário.
# 
# Vamos explorar este conceito através de alguns exemplos:

# In[1]:


import numpy as np
import pandas as pd


# ### Criando uma Serie
# 
# Você pode converter uma lista, numpy array ou dicionário para uma série:

# In[2]:


labels = ['a','b','c']
minha_lista = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}


# ** Usando listas **

# In[3]:


pd.Series(data=minha_lista)


# In[4]:


pd.Series(data=minha_lista,index=labels)


# In[5]:


pd.Series(minha_lista,labels)


# ** NumPy Arrays **

# In[6]:


pd.Series(arr)


# In[7]:


pd.Series(arr,labels)


# ** Dicionários **

# In[8]:


pd.Series(d)


# ### Dados nas Series
# 
# Uma série de pandas pode conter uma variedade de tipos de objeto:

# In[9]:


pd.Series(data=labels)


# In[10]:


# Mesmo funções (embora seja improvável que você use isso)
pd.Series([sum,print,len])


# ## Usando um Índice
# 
# A chave para usar uma Serie é entender seu índice. O Pandas faz uso desses nomes ou números de índice, permitindo pesquisas rápidas de informações (funciona como uma tabela de hash ou dicionário).
# 
# Vamos ver alguns exemplos de como pegar informações de uma Serie. Vamos criar duas Series, ser1 e ser2:

# In[17]:


ser1 = pd.Series([1,2,3,4],index = ['EUA', 'Alemanha','USSR', 'Japão'])                                   


# In[18]:


ser1


# In[19]:


ser2 = pd.Series([1,2,5,4],index = ['EUA', 'Alemanha','Italia', 'Japão'])                                   


# In[20]:


ser2


# In[21]:


ser1['EUA']


# As operações também são feitas com base no índice:

# In[22]:


ser1 + ser2


# Vamos parar aqui por enquanto e passar para a DataFrames, que expandirá o conceito da Serie!
