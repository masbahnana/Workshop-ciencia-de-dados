#!/usr/bin/env python
# coding: utf-8

# # NumPy 
# 
# NumPy (ou Numpy) é uma biblioteca de álgebra linear para Python, a razão pela qual é tão importante para a Data Science com Python é que quase todas as bibliotecas dependem do NumPy como um dos seus principais blocos de construção.
# 
# Numpy também é incrivelmente rápido, pois tem ligações para bibliotecas C. Para obter mais informações sobre por que você deseja usar Arrays em vez de listas, confira esta excelente publicação do [StackOverflow post](http://stackoverflow.com/questions/993984/why-numpy-instead-of-python-lists).
# 
# Nós só aprenderemos os conceitos básicos do NumPy, para começar, precisamos instalá-lo!

# ## Instruções de instalação
# 
# ** É altamente recomendável que instale o Python usando a distribuição da Anaconda para garantir que todas as dependências subjacentes (como as bibliotecas de Álgebra Linear) se sincronizem com o uso de uma instalação conda. Se você tiver o Anaconda, instale o NumPy acessando seu terminal ou prompt de comando e digite: **
# 
#     conda install numpy
#     
# ** Se você não possui Anaconda e não pode instalá-lo, consulte: [Numpy's official documentation on various installation instructions.](http://docs.scipy.org/doc/numpy-1.10.1/user/install.html)**

# ## Usando NumPy
# 
# Depois de instalar o NumPy, você pode importá-lo como uma biblioteca:

# In[4]:


import numpy as np


# Numpy possui muitas funções e capacidades incorporadas. Não vamos cobri-los na totalidade, mas, em vez disso, vamos nos concentrar em alguns dos aspectos mais importantes de Numpy: vetores, arrays, matrizes e geração de números. Comecemos por arrays:
# 
# # Numpy Arrays
# 
# As matrizes de NumPy são a maneira principal de usar Numpy ao longo do curso. Numpy arrays essencialmente vêm de duas formas: vetores e matrizes. Os vetores são estritamente arranjos de 1d e as matrizes são 2d (mas você deve observar que uma matriz ainda pode ter apenas uma linha ou uma coluna).
# 
# Vamos começar nossa introdução explorando como criar matrizes numPy.
# 
# 
# ## Criando NumPy Arrays
# 
# ### De uma lista de Python
# 
# Podemos criar uma matriz convertendo diretamente uma lista ou lista de listas:

# In[5]:


minha_lista = [1,2,3]
minha_lista


# In[6]:


np.array(minha_lista)


# In[7]:


minha_matriz = [[1,2,3],[4,5,6],[7,8,9]]
minha_matriz


# In[8]:


np.array(minha_matriz)


# ## Métodos incorporados (Built-in Methods)
# 
# Há muitas maneiras embutidas de gerar Arrays

# ### arange
# 
# Retorna valores uniformemente espaçados dentro de um determinado intervalo.

# In[9]:


np.arange(0,10)


# In[10]:


np.arange(0,11,2)


# ### zeros e ones
# 
# Gerar matrizes de zeros ou de ums

# In[11]:


np.zeros(3)


# In[12]:


np.zeros((5,5))


# In[13]:


np.ones(3)


# In[14]:


np.ones((3,3))


# ### linspace
# Retorna números uniformemente espaçados ao longo de um intervalo especificado.

# In[15]:


np.linspace(0,10,3)


# In[16]:


np.linspace(0,10,50)


# ## eye
# 
# Cria uma matriz identidade

# In[17]:


np.eye(4)


# ## Random 
# 
# Numpy também tem muitas maneiras de criar arrays de números aleatórios:
# 
# ### rand
# Cria uma matriz da forma dada e preencha com amostras aleatórias de uma distribuição uniforme sobre ``[0, 1)``.

# In[20]:


np.random.rand(2)


# In[21]:


np.random.rand(5,5)


# ### randn
# 
# Retorna uma amostra (ou amostras) da distribuição "normal". Ao contrário de rand, que é uniforme:

# In[22]:


np.random.randn(2)


# In[23]:


np.random.randn(5,5)


# ### randint
# Retorna inteiros aleatórios de "low" (inclusive) para "high" (exclusivo).

# In[24]:


np.random.randint(1,100)


# In[25]:


np.random.randint(1,100,10)


# ## Atributos de Array e Métodos
# 
# Vamos discutir alguns atributos e métodos úteis ou uma matriz:

# In[26]:


arr = np.arange(25)
ranarr = np.random.randint(0,50,10)


# In[27]:


arr


# In[28]:


ranarr


# ## Reshape
# Retorna uma matriz contendo os mesmos dados com uma nova forma.

# In[29]:


arr.reshape(5,5)


# ### max,min,argmax,argmin
# 
# Estes são métodos úteis para encontrar valores máximos ou mínimos, ou para encontrar seus locais de índice usando argmin ou argmax

# In[30]:


ranarr


# In[31]:


ranarr.max()


# In[32]:


ranarr.argmax()


# In[33]:


ranarr.min()


# In[34]:


ranarr.argmin()


# ## Shape
# 
# Shape é um atributo que os arrays têm (não um método):

# In[35]:


# Vector
arr.shape


# In[36]:


arr.reshape(1,25)


# In[37]:


arr.reshape(1,25).shape


# In[38]:


arr.reshape(25,1)


# In[39]:


arr.reshape(25,1).shape


# ### dtype
# Você também pode pegar o tipo de dados do objeto na matriz:

# In[40]:


arr.dtype

