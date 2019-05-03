#!/usr/bin/env python
# coding: utf-8

# # PairGrids
# 
# Os PairGrids são tipos gerais de gráficos que permitem mapear tipos de plotagem diferentes para linhas e colunas de um grid, isso ajuda você a criar plots similares separadas por categoias.

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


iris = sns.load_dataset('iris')


# In[3]:


iris.head()


# ## PairGrid
# 
# Pairgrid é um plot de grade para traçar relacionamentos entre pares de um conjunto de dados.

# In[11]:


# Just the Grid
sns.PairGrid(iris)


# In[26]:


# Then you map to the grid
g = sns.PairGrid(iris)
g.map(plt.scatter)


# In[8]:


# Altera os tipos de plots na diagonal, parte superior e inferior.
g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)


# ## pairplot
# 
# Pairplot é uma versão mais simples do PairGrid (você usará com bastante frequência)

# In[12]:


sns.pairplot(iris)


# In[13]:


sns.pairplot(iris,hue='species',palette='rainbow')


# ## FacetGrid
# 
# FacetGrid é a maneira geral de criar plots de grades com base em um recurso:

# In[14]:


tips = sns.load_dataset('tips')


# In[15]:


tips.head()


# In[16]:


# Só a grade
g = sns.FacetGrid(tips, col="time", row="smoker")


# In[17]:


g = sns.FacetGrid(tips, col="time",  row="smoker")
g = g.map(plt.hist, "total_bill")


# In[18]:


g = sns.FacetGrid(tips, col="time",  row="smoker",hue='sex')
# Observe como os argumentos vêm após a chamada do plt.scatter
g = g.map(plt.scatter, "total_bill", "tip").add_legend()


# ## JointGrid
# 
# JointGrid é a versão geral para grades tipo jointplot (), para um exemplo rápido:

# In[19]:


g = sns.JointGrid(x="total_bill", y="tip", data=tips)


# In[20]:


g = sns.JointGrid(x="total_bill", y="tip", data=tips)
g = g.plot(sns.regplot, sns.distplot)


# Consulte a documentação conforme necessário para os tipos de grade, mas na maioria das vezes você apenas usará os gráficos mais simples discutidos anteriormente.
