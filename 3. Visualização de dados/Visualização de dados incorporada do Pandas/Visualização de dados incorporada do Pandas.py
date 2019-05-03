#!/usr/bin/env python
# coding: utf-8

# # Visualização de dados incorporada do Pandas
# 
# Nesta palestra, aprenderemos sobre capacidades integradas de pandas para visualização de dados. É construído em matplotlib, mas foi inserido no pandas para um uso mais fácil!
# 
# Vamos dar uma olhada!

# ## Imports

# In[2]:


import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Os dados
# 
# Existem alguns arquivos csv de dados falsos que você pode ler como dados:

# In[3]:


df1 = pd.read_csv('df1',index_col=0)
df2 = pd.read_csv('df2')


# ## Folhas de estilo
# 
# Matplotlib tem [folhas de estilo](http://matplotlib.org/gallery.html#style_sheets) que você pode usar para tornar seus plots mais agradáveis. Essas folhas de estilo incluem plot_bmh, plot_fivethirtyeight, plot_ggplot e muito mais. Eles basicamente criam um conjunto de regras de estilo que seus plots seguirão. Eu recomendo usá-los dado que eles farão seus plots terem uma aparência muito mais profissional. Você pode até mesmo criar o seu próprio caso você deseja que os gráficos de sua empresa tenham todos o mesmo aspecto (é um pouco tedioso para criar).
# 
# Aqui é como usá-los.
# 
# ** Antes de plt.style.use (), seus plots são assim: **

# In[4]:


df1['A'].hist()


# Aplicando o estilo:

# In[5]:


import matplotlib.pyplot as plt
plt.style.use('ggplot')


# Now your plots look like this:

# In[6]:


df1['A'].hist()


# In[7]:


plt.style.use('bmh')
df1['A'].hist()


# In[8]:


plt.style.use('dark_background')
df1['A'].hist()


# In[9]:


plt.style.use('fivethirtyeight')
df1['A'].hist()


# In[10]:


plt.style.use('ggplot')


# Vamos ficar com o estilo ggplot e, na verdade, mostramos como utilizar os recursos de traçabilidade embutidos no pandas!

# # Tipos de plotagem
# 
# Existem vários tipos de plots incorporados aos pandas, a maioria deles plots estatísticos por natureza:
# 
# * df.plot.area
# * df.plot.barh
# * df.plot.density
# * df.plot.hist
# * df.plot.line
# * df.plot.scatter
# * df.plot.bar
# * df.plot.box
# * df.plot.hexbin
# * df.plot.kde
# * df.plot.pie
# 
# Você também pode simplesmente chamar df.plot (kind = 'hist') ou substituir esse argumento por qualquer um dos termos-chave mostrados na lista acima (por exemplo, 'caixa', 'barh', etc.)
# ___

# Vamos começar por eles!
# 
# ## Área

# In[11]:


df2.plot.area(alpha=0.4)


# ## Barplots

# In[12]:


df2.head()


# In[13]:


df2.plot.bar()


# In[14]:


df2.plot.bar(stacked=True)


# ## Histogramas

# In[15]:


df1['A'].plot.hist(bins=50)


# ## Line Plots

# In[16]:


df1.plot.line(x=df1.index,y='B',figsize=(12,3),lw=1)


# ## Scatter Plots

# In[17]:


df1.plot.scatter(x='A',y='B')


# Você pode usar c para colorir com base em outro valor de coluna.
# Use o cmap para indicar o mapa de cores a ser usado.
# Para todos os colormaps, confira: http://matplotlib.org/users/colormaps.html

# In[18]:


df1.plot.scatter(x='A',y='B',c='C',cmap='coolwarm')


# Ou use s para indicar o tamanho com base em outra coluna. s parâmetro precisa ser uma matriz, não apenas o nome de uma coluna:

# In[20]:


df1.plot.scatter(x='A',y='B',s=df1['C']*200)


# ## BoxPlots

# In[22]:


df2.plot.box()


# ## Hexagonal Bin Lote
# 
# Útil para Dados Bivariados, alternativa ao Scatterplot:

# In[23]:


df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df.plot.hexbin(x='a',y='b',gridsize=25,cmap='Oranges')


# ____

# ## Plot de Estimação de densidade de Kernel (Kernel Density Estimation - KDE)

# In[24]:


df2['a'].plot.kde()


# In[25]:


df2.plot.density()


# É isso aí! Espero que você possa ver por que esse método de traçado será muito mais fácil de usar do que full-on matplotlib, ele equilibra a facilidade de uso com controle sobre a figura. Muitas dos plots também aceitam argumentos adicionais de sua matriz matplotlib plt. ligar.
# 
# Em seguida, vamos aprender sobre seaborn, que é uma biblioteca de visualização estatística projetada para trabalhar bem com os quadros de dados do pandas.
# 
# Antes disso, porém, teremos um exercício rápido para você!
# 
# # Bom trabalho!
