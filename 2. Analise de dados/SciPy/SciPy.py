#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # SciPy
# 
# SciPy é uma coleção de algoritmos matemáticos e funções de conveniência construídas sob Numpy do Python. Ele adiciona poder significativo para a sessão interativa de Python, fornecendo ao usuário comandos e classes de alto nível para manipular e visualizar dados. Com o SciPy, uma sessão interativa de Python torna-se um ambiente de processamento de dados e prototipagem do sistema que rivaliza com sistemas como MATLAB, IDL, Octave, R-Lab e SciLab.
# 
# O benefício adicional de basar SciPy no Python é que isso também faz uma poderosa linguagem de programação disponível para o desenvolvimento de programas sofisticados e aplicativos especializados.
# 
# Tudo, desde programação paralela até sub-rotinas de base de dados e base de dados, foi disponibilizado ao programador Python. Todo esse poder está disponível além das bibliotecas matemáticas no SciPy.
# 
# Vamos focar muito mais nas matrizes NumPy, mas vamos mostrar algumas das capacidades do SciPy:

# In[1]:


import numpy as np
A = np.array([[1,2,3],[4,5,6],[7,8,8]])


# ## Algebra Linear
# **linalg**

# In[2]:


from scipy import linalg


# Determinante de uma matriz

# In[3]:


# Calcule o determinante de uma matriz
linalg.det(A)


# Calcule a decomposição de LU girada de uma matriz.
# 
# A decomposição é ::
# 
#     A = P L U
# 
# Onde P é uma matriz de permutação, L triangular inferior com elementos diagonais da unidade e U triangular superior.

# In[4]:


P, L, U = linalg.lu(A)


# In[5]:


P


# In[6]:


L


# In[7]:


U


# In[8]:


np.dot(L,U)


# Podemos descobrir os autovalores e os vetores próprios desta matriz:

# In[9]:


EW, EV = linalg.eig(A)


# In[10]:


EW


# In[11]:


EV


# A solução de sistemas de equações lineares também pode ser feita:

# In[12]:


v = np.array([[2],[3],[5]])


# In[13]:


v


# In[14]:


s = linalg.solve(A,v)


# In[15]:


s


# ## Álgebra Linear Esparsa
# SciPy possui algumas rotinas para computação com matrizes esparsas e potencialmente muito grandes. As ferramentas necessárias estão no submodulo scipy.sparse.
# 
# Nós fazemos um exemplo sobre como construir uma matriz grande:

# In[16]:


from scipy import sparse


# In[17]:


A = sparse.lil_matrix((1000, 1000))


# In[18]:


A


# In[19]:


A[0,:100] = np.random.rand(100)


# In[20]:


A[1,100:200] = A[0,:100]


# In[21]:


A.setdiag(np.random.rand(1000))


# In[22]:


A


# **Algebra linear com matrizes esparsas**

# In[23]:


from scipy.sparse import linalg


# In[24]:


# Converte esta matriz para o formato linha esparsa comprimida.
A.tocsr()


# In[25]:


A = A.tocsr()


# In[26]:


b = np.random.rand(1000)


# In[27]:


linalg.spsolve(A, b)


# Há muito mais que SciPy é capaz de, como Transformadas de Fourier, Funções de Bessel, etc ...
# 
# Dê uma olhada na Documentação para mais detalhes!
