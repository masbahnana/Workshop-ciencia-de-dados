#!/usr/bin/env python
# coding: utf-8

# # Mesclar, Juntar, e Concatenar
# 
# There are 3 main ways of combining DataFrames together: Merging, Joining and Concatenating. In this lecture we will discuss these 3 methods with examples.
# 
# Existem três maneiras principais de combinar os DataFrames: mesclando, juntando e concatenando (merge, join e concat). Nesta palestra, discutiremos esses 3 métodos com exemplos.
# 
# ____

# ### Exemplos de DataFrames

# In[1]:


import pandas as pd


# In[2]:


df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])


# In[3]:


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 


# In[4]:


df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])


# In[5]:


df1


# In[6]:


df2


# In[7]:


df3


# ## Concatenação
# 
# Concatenação basicamente cola DataFrames. Tenha em mente que as dimensões devem corresponder ao longo do eixo que você está concatenando. Você pode usar ** pd.concat ** e passar uma lista de DataFrames para concatenar juntos:

# In[8]:


pd.concat([df1,df2,df3])


# In[9]:


pd.concat([df1,df2,df3],axis=1)


# _____
# ## Outros DataFrames

# In[2]:


esquerda = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
direita = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})    


# In[3]:


esquerda


# In[4]:


direita


# ## Mesclar
# 
# A função ** mesclar ** permite que você mescle os quadros de dados juntos usando uma lógica semelhante à mesclagem de tabelas SQL juntas. Por exemplo:

# In[5]:


pd.merge(esquerda,direita,how='inner',on='key')


# Ou para mostrar um exemplo mais complicado:

# In[6]:


esquerda = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
direita = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})


# In[7]:


pd.merge(esquerda, direita, on=['key1', 'key2'])


# In[18]:


pd.merge(esquerda, direita, how='outer', on=['key1', 'key2'])


# In[19]:


pd.merge(esquerda, direita, how='right', on=['key1', 'key2'])


# In[20]:


pd.merge(esquerda, direita, how='left', on=['key1', 'key2'])


# ## Juntar
# Juntar é um método conveniente para combinar as colunas de dois DataFrames indexados potencialmente diferentes em um único resultado DataFrame.

# In[9]:


esquerda = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

direita = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])


# In[11]:


esquerda


# In[12]:


direita


# In[22]:


esquerda.join(direita)


# In[23]:


esquerda.join(direita, how='outer')

