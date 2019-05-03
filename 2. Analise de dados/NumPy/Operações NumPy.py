#!/usr/bin/env python
# coding: utf-8

# # Operações NumPy

# ## Operações artiméticas
# 
# Você pode facilmente executar operaões aritméticas com matrizes ou escalar. Vamos ver alguns exemplos:

# In[1]:


import numpy as np
arr = np.arange(0,10)


# In[2]:


arr + arr


# In[3]:


arr * arr


# In[4]:


arr - arr


# In[5]:


# Aviso na divisão por zero, mas não um erro!
# Apenas substituído por nan
arr/arr


# In[6]:


# Também aviso, mas não um erro, apenas infinito
1/arr


# In[7]:


arr**3


# ## Funções da matriz universal
# 
# Numpy vem com muitas [funções universais de matrizes](http://docs.scipy.org/doc/numpy/reference/ufuncs.html), que são essenciais nas apenas operações matemáticas que você pode usar para executar operalções em toda  matriz. Vamos mostrar as mais comuns:

# In[8]:


# Tomando raízes quadradas
np.sqrt(arr)


# In[9]:


# Calculando exponenciais (e^)
np.exp(arr)


# In[10]:


np.max(arr) # O mesmo que arr.max()


# In[11]:


np.sin(arr)


# In[12]:


np.log(arr)

