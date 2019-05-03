#!/usr/bin/env python
# coding: utf-8

# # Plots de regressões
# 
# O Seaborn possui muitas ferramentas integradas para plots de regressão, no entanto, não discutiremos a regressão até a seção de Machine Learning do curso, de modo que apenas cobriremos a função ** lmplot () ** por enquanto.
# 
# ** lmplot ** permite que você exiba modelos lineares, mas também permite que você divida esses gráficos com base em recursos, além de colorir a matiz de cores com base nos recursos.
# 
# Vamos explorar como isso funciona:
# 

# In[1]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


tips = sns.load_dataset('tips')


# In[3]:


tips.head()


# ## lmplot()

# In[4]:


sns.lmplot(x='total_bill',y='tip',data=tips)


# In[5]:


sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')


# In[6]:


sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm')


# ### Trabalhando com marcadores
# 
# lmplot kwargs são passados através do ** regplot **, que é uma forma mais geral de lmplot (). O regplot possui um parâmetro scatter_kws é passado para plt.scatter. Então, você pode querer definir o parâmetro "s" nesse dicionário, o que corresponde ao tamanho dos marcadores. Em outras palavras, você acaba passando um dicionário com os argumentos base do matplotlib, neste caso, s para o tamanho do gráfico de dispersão. Em geral, você provavelmente não vai se lembrar disso sempre, porém, consulte sempre que achar necessário.

# In[7]:


# http://matplotlib.org/api/markers_api.html
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='coolwarm',
           markers=['o','v'],scatter_kws={'s':100})


# ## Usando grades
# 
# Podemos adicionar mais separação variável através de colunas e linhas com o uso de uma grade. Basta indicar isso com os argumentos col ou row:

# In[8]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='sex')


# In[9]:


sns.lmplot(x="total_bill", y="tip", row="sex", col="time",data=tips)


# In[10]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm')


# ## Aspecto e tamanho
# 
# As figuras de Seaborn podem ter seu tamanho e aspect ajustados com os parâmetros ** ** size ** e ** aspecto **:

# In[11]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',palette='coolwarm',
          aspect=0.6,size=8)


# Se desejar obter mais informações sobre como alterar outros aspectos visuais dos seus plots no seaborn, confira o Notebook sobre o assunto!
