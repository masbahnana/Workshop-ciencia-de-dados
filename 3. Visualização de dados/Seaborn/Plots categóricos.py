#!/usr/bin/env python
# coding: utf-8

# # Plots categóricos
# 
# Agora vamos discutir como usar seaborn para traçar dados categóricos. Existem alguns tipos de argumentos principais para isso:
# 
# * factorplot
# * boxplot
# * violinplot
# * stripplot
# * swarmplot
# * barplot
# * countplot
# 
# Vamos passar por exemplos de cada um.

# In[1]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


tips = sns.load_dataset('tips')
tips.head()


# ## barplot e countplot
# 
# Esses plots parecidos permitem que você obtenha dados agregados de um recurso categórico. ** barplot ** é um gráfico geral que permite que você agregue os dados categóricos baseados em alguma função, por padrão, a média:

# In[4]:


sns.barplot(x='sex',y='total_bill',data=tips)


# In[5]:


import numpy as np


# Você pode alterar o objeto estimador para sua própria função, que converte um vetor em um escalar:

# In[6]:


sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)


# ### countplot
# 
# Isto é essencialmente o mesmo que o gráfico de barras, exceto que o estimador está explicitamente contando o número de ocorrências. É por isso que apenas passamos o valor x:

# In[7]:


sns.countplot(x='sex',data=tips)


# ## boxplot and violinplot
# 
# Boxplots e violinplots são usados para mostrar a distribuição de dados categóricos. Um boxplot (ou gráfico de caixa e espessura) mostra a distribuição de dados quantitativos de uma maneira que facilita comparações entre variáveis ou entre os níveis de uma variável categórica. A caixa mostra os quartis do conjunto de dados, enquanto as barras se estendem para mostrar o resto da distribuição, exceto pelos pontos que são determinados como "outliers".

# In[22]:


sns.boxplot(x="day", y="total_bill", data=tips,palette='rainbow')


# In[8]:


# Podemos orientar os dados para aparecerem na horizontal
sns.boxplot(data=tips,palette='rainbow',orient='h')


# In[9]:


sns.boxplot(x="day", y="total_bill", hue="smoker",data=tips, palette="coolwarm")


# ### violinplot
# 
# Um violinplot desempenha um papel semelhante a um boxplot. Ele mostra a distribuição de dados quantitativos em vários níveis de uma (ou mais) variáveis categóricas, de modo que essas distribuições possam ser comparadas. Ao contrário de um boxplot, no qual todos os componentes do gráfico correspondem a pontos de dados reais, o gráfico de violino possui uma estimativa da densidade do núcleo da distribuição subjacente.

# In[10]:


sns.violinplot(x="day", y="total_bill", data=tips,palette='rainbow')


# In[11]:


sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',palette='Set1')


# In[12]:


sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',split=True,palette='Set1')


# ## stripplot e swarmplot
# 
# O stripplot irá desenhar um scatterplot onde uma variável é categórica. Um stripplot pode ser desenhado por conta própria, mas também é um bom complemento para uma boxplot ou violinplot nos casos em que você deseja mostrar todas as observações juntamente com alguma representação da distribuição subjacente.
# 
# O swarmplot é semelhante ao stripplot (), mas os pontos são ajustados (somente ao longo do eixo categórico) para que eles não se sobreponham. Isso dá uma melhor representação da distribuição de valores, embora não se ajude também a um grande número de observações (tanto em termos de capacidade de mostrar todos os pontos quanto em termos da computação necessária para organizá-los).

# In[13]:


sns.stripplot(x="day", y="total_bill", data=tips)


# In[14]:


sns.stripplot(x="day", y="total_bill", data=tips,jitter=True)


# In[15]:


sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1')


# In[16]:


sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1',split=True)


# In[17]:


sns.swarmplot(x="day", y="total_bill", data=tips)


# In[47]:


sns.swarmplot(x="day", y="total_bill",hue='sex',data=tips, palette="Set1", split=True)


# ### Combinando plots categóricos

# In[18]:


sns.violinplot(x="tip", y="day", data=tips,palette='rainbow')
sns.swarmplot(x="tip", y="day", data=tips,color='black',size=3)


# ## factorplot
# 
# O factorplot é a forma mais geral de um plot categórico. Pode aceitar um parâmetro ** kind ** para ajustar o tipo de plotagem:

# In[19]:


sns.factorplot(x='sex',y='total_bill',data=tips,kind='bar')

