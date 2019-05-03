#!/usr/bin/env python
# coding: utf-8

# # Plots matriciais
# 
# Os gráficos matriciais permitem traçar dados como matrizes codificadas por cores e também podem ser usados para indicar clusters dentro dos dados (mais tarde, na seção de Machine Learning, aprenderemos a formatear dados de cluster).
# 
# Comecemos por explorar o mapa térmico e o clutermap de Seaborn:

# In[1]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


flights = sns.load_dataset('flights')


# In[3]:


tips = sns.load_dataset('tips')


# In[4]:


tips.head()


# In[5]:


flights.head()


# ## Heatmap
# 
# Para que um mapa de calor funcione corretamente, seus dados já devem estar em uma forma de matriz e a função sns.heatmap basicamente apenas põe cor pra você. Por exemplo:

# In[6]:


tips.head()


# In[7]:


# Correlograma
tips.corr()


# In[8]:


sns.heatmap(tips.corr())


# In[9]:


sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)


# Ou para os dados dos vôos:

# In[10]:


flights.pivot_table(values='passengers',index='month',columns='year')


# In[11]:


pvflights = flights.pivot_table(values='passengers',index='month',columns='year')
sns.heatmap(pvflights)


# In[12]:


sns.heatmap(pvflights,cmap='magma',linecolor='white',linewidths=1)


# ## clustermap
# 
# O clustermap usa agrupamento hierárquico para produzir uma versão em cluster do heatmap. Por exemplo:

# In[13]:


sns.clustermap(pvflights, standard_scale=1)


# Observe agora como os anos e os meses não estão mais em ordem, em vez disso, eles são agrupados por similaridade em valor (contagem de passageiros). Isso significa que podemos começar a inferir coisas desse plot, como agosto e julho sendo semelhantes (faz sentido, uma vez que são ambos os meses de viagem de verão no hemisfério norte)

# In[14]:


# Mais opções para obter a informação um pouco mais clara, como a normalização
sns.clustermap(pvflights,cmap='coolwarm',standard_scale=1)

