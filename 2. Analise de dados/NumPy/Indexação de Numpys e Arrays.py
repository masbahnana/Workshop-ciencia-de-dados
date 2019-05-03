#!/usr/bin/env python
# coding: utf-8

# # Indexação de Numpys e Arrays
# 
# Nesta palestra, vamos discutir como selecionar elementos ou grupos de elementos de uma matriz.

# In[1]:


import numpy as np


# In[2]:


# Criando um simples array
arr = np.arange(0,11)


# In[3]:


# Mostrar
arr


# ## Indexação e seleção
# A maneira mais simples de escolher um ou alguns elementos de uma matriz é muito semelhante às listas de python:

# In[4]:


# Obtendo um valor através de um índice
arr[8]


# In[5]:


# Obtendo valores em um intervalo
arr[1:5]


# In[6]:


arr[0:5]


# ## Transmissão
# 
# Numpy arrays diferem de uma lista Python normal por causa de sua capacidade de transmissão:

# In[7]:


# Configurando um valor com intervalo de índice (Transmissão)
arr[0:5]=100

#Show
arr


# In[8]:


# Redefinir matriz, veremos por que eu tive que redefinir em um momento
arr = np.arange(0,11)

# Mostrando
arr


# In[10]:


# Notas importantes sobre fatias
slice_de_arr = arr[0:6]

# Mostra a fatia
slice_de_arr


# In[11]:


# Modifica a fatia
slice_de_arr[:]=99

#Show Slice again
slice_de_arr


# Agora note que as mudanças também ocorrem em nossa matriz original!

# In[12]:


arr


# Os dados não são copiados, é uma visão da matriz original! Isso evita problemas de memória!

# In[13]:


# Para obter uma cópia, precisa ser explícito
arr_copy = arr.copy()

arr_copy


# ## Indexando uma matriz 2D
# 
# O formato geral é ** arr_2d [row] [col] ** ou ** arr_2d [row, col] **. Eu recomendo geralmente usando a notação de vírgula para maior clareza.

# In[14]:


arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))

# Mostrando
arr_2d


# In[15]:


# Fila de indexação
arr_2d[1]


# In[16]:


# O formato é arr_2d [row] [col] ou arr_2d [row, col]

# Obtendo o valor do elemento individual
arr_2d[1][0]


# In[17]:


# Obtendo o valor do elemento individual
arr_2d[1,0]


# In[18]:


# Fatiando um array 2D

# Fatia (2,2) do canto superior direito
arr_2d[:2,1:]


# In[19]:


# Fatia inferior
arr_2d[2]


# In[20]:


# Fatia inferior
arr_2d[2,:]


# ### Indexação "Fancy"
# 
# A indxação "Fancy" permite que você selecione linhas inteiras ou colunas fora de ordem, para mostrar isso, vamos construir rapidamente uma matriz numpy:

# In[21]:


arr2d = np.zeros((10,10))


# In[22]:


# Tamaho do array
arr_length = arr2d.shape[1]


# In[23]:


for i in range(arr_length):
    arr2d[i] = i
    
arr2d


# Indexação "Fancy" permite o seguinte:

# In[24]:


arr2d[[2,4,6,8]]


# In[25]:


# Permite em qualquer ordem
arr2d[[6,4,2,7]]


# ## Mais Ajuda de Indexação
# A indexação de uma matriz 2d pode ser um pouco confusa no início, especialmente quando você começa a adicionar em tamanho de etapa. Experimente pesquisar no Google "indexação NumPy" para imagens úteis, como esta:
# 
# <img src= 'http://memory.osu.edu/classes/python/_images/numpy_indexing.png' width=500/>

# ## Seleção
# 
# Vamos examinar brevemente como usar colchetes para seleção com base em operadores de comparação.

# In[26]:


arr = np.arange(1,11)
arr


# In[27]:


arr > 4


# In[28]:


bool_arr = arr>4


# In[29]:


bool_arr


# In[30]:


arr[bool_arr]


# In[31]:


arr[arr>2]


# In[32]:


x = 2
arr[arr>x]

