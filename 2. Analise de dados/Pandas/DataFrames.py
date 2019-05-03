#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # DataFrames
# 
# DataFrame é o elemeto mais importante dos Pandas e são diretamente inspirados pela linguagem de programação R. Podemos pensar em um DataFrame como um monte de objetos da série juntos para compartilhar o mesmo índice. Vamos usar Pandas para explorar esse tópico!

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


from numpy.random import randn
np.random.seed(101)


# In[5]:


df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())


# In[6]:


df


# ## Seleção e indexação
# 
# Vamos aprender os vários métodos para pegar dados de um DataFrame

# In[7]:


df['W']


# In[8]:


# Passando uma lista com nomes das colunas
df[['W','Z']]


# In[9]:


# Sintaxe SQL (Não recomendado!)
df.W


# As colunas dos DataFrames são Series

# In[10]:


type(df['W'])


# ** Criando uma coluna: **

# In[11]:


df['new'] = df['W'] + df['Y']


# In[12]:


df


# ** Removendo colunas **

# In[13]:


df.drop('new',axis=1)


# In[14]:


# Porém, tal exclusão só ocorrerá se especificada no parâmetro inplace
df


# In[15]:


df.drop('new',axis=1,inplace=True)


# In[16]:


df


# Também podemos deletar colunas desta forma:

# In[17]:


df.drop('E',axis=0)


# ** Selecionando linhas: **

# In[198]:


df.loc['A']


# Ou selecione com base na posição em vez do rótulo

# In[18]:


df.iloc[2]


# ** Selecionando o subconjunto de linhas e colunas **

# In[19]:


df.loc['B','Y']


# In[20]:


df.loc[['A','B'],['W','Y']]


# ### Seleção condicional
# 
# Uma característica importante dos pandas é a seleção condicional usando notação de colchetes, muito semelhante ao numpy:

# In[21]:


df


# In[22]:


df>0


# In[23]:


df[df>0]


# In[24]:


df[df['W']>0]


# In[25]:


df[df['W']>0]['Y']


# In[26]:


df[df['W']>0][['Y','X']]


# Para duas condições, você pode usar | e & com parênteses:

# In[27]:


df[(df['W']>0) & (df['Y'] > 1)]


# ## Mais Detalhes do Índice
# 
# Vamos discutir mais alguns recursos de indexação, incluindo resetar o índice ou configurá-lo de outra forma. Também falaremos sobre hierarquia de índice!

# In[28]:


df


# In[29]:


# Redefinir para o padrão 0,1 ... n índice
df.reset_index()


# In[30]:


novoind = 'CA NY WY OR CO'.split()


# In[32]:


df['Estados'] = novoind


# In[33]:


df


# In[34]:


df.set_index('Estados')


# In[35]:


df


# In[36]:


df.set_index('Estados',inplace=True)


# In[37]:


df


# ## Hierarquia de índices e índices múltiplos
# 
# Vamos examinar como trabalhar com o Multi-Index, primeiro criaremos um exemplo rápido de como seria um DataFrame Multi-Indexado:

# In[39]:


# Níveis de Índice
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[40]:


hier_index


# In[41]:


df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df


# Agora vamos mostrar como indexar isso! Para a hierarquia de índice, usamos df.loc []. Se este fosse no eixo das colunas, você usaria a notação de suporte normal df []. Chamar um nível do índice retorna um sub-dataframe:

# In[42]:


df.loc['G1']


# In[43]:


df.loc['G1'].loc[1]


# In[44]:


df.index.names


# In[45]:


df.index.names = ['Grupo','Número']


# In[46]:


df


# In[47]:


df.xs('G1')


# In[48]:


df.xs(['G1',1])


# In[49]:


df.xs(1,level='Número')

