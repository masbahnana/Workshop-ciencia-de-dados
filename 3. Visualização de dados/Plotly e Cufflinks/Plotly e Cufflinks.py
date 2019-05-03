#!/usr/bin/env python
# coding: utf-8

# # Plotly e Cufflinks

# O Plotly é uma biblioteca que permite criar gráficos interativos que você pode usar em painéis ou sites (você pode salvá-los como arquivos html ou imagens estáticas).
# 
# ## Instalação
# 
# Para que tudo funcione, você precisará instalar plotly e cufflinks para chamar plots diretamente de um DataFrame pandas. Essas bibliotecas não estão atualmente disponíveis através de ** conda **, mas estão disponíveis através de ** pip **. Instale as bibliotecas em sua linha de comando / terminal usando:
# 
#     pip install plotly
#     pip install cufflinks
# 
# ** NOTA: Certifique-se de ter apenas uma instalação do Python no seu computador quando faz isso, caso contrário, a instalação pode não funcionar. **
# 
# ## Importações e Configuração

# In[11]:


import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print(__version__)


# In[13]:


import cufflinks as cf


# In[14]:


# Para Notebooks
init_notebook_mode(connected=True)


# In[15]:


# For offline use
cf.go_offline()


# ### Dados forjados

# In[16]:


df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())


# In[17]:


df.head()


# In[18]:


df2 = pd.DataFrame({'Categoria':['A','B','C'],'Valores':[32,43,50]})


# In[19]:


df2.head()


# ## Usando Cufflinks e iplot ()
# 
# * Dispersão
# * Barras
# * BoxPlot
# * Spreads
# * Proporção
# * Mapa de calor
# * Superfícies 3D
# * Histograma
# * Bolha

# ## Dispersão

# In[20]:


df.iplot(kind='scatter',x='A',y='B',mode='markers',size=10)


# ## Plots de barra

# In[22]:


df2.iplot(kind='bar',x='Categoria',y='Valores')


# In[23]:


df.count().iplot(kind='bar')


# ## Boxplots

# In[24]:


df.iplot(kind='box')


# ## Superfícies 3D

# In[25]:


df3 = pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[5,4,3,2,1]})
df3.iplot(kind='surface',colorscale='rdylbu')


# ## Spread

# In[26]:


df[['A','B']].iplot(kind='spread')


# ## Histograma

# In[28]:


df['A'].iplot(kind='hist',bins=25)


# ## Bolha

# In[31]:


df.iplot(kind='bubble',x='A',y='B',size='C')


# ## scatter_matrix()
# 
# Similar à sns.pairplot()

# In[32]:


df.scatter_matrix()

