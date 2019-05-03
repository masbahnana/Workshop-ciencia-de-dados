#!/usr/bin/env python
# coding: utf-8

# # Estilos e cores
# 
# Nós mostramos anteriormente como controlar a estética da figura em Seaborn, mas vamos agora examiná-lo formalmente:

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
tips = sns.load_dataset('tips')


# ## Styles
# 
# Você pode definir um estilo específico.

# In[2]:


sns.countplot(x='sex',data=tips)


# In[3]:


sns.set_style('white')
sns.countplot(x='sex',data=tips)


# In[4]:


sns.set_style('ticks')
sns.countplot(x='sex',data=tips,palette='deep')


# ## Remoção dos limites

# In[5]:


sns.countplot(x='sex',data=tips)
sns.despine()


# In[6]:


sns.countplot(x='sex',data=tips)
sns.despine(left=True)


# ## Tamanho e aspecto

# Você pode usar o ** plt.figure do matplotlib (figsize = (width, height) ** para alterar o tamanho da maioria dos gráficos do seaborn.
# 
# Você pode controlar a proporção de tamanho e aspecto da maioria dos plots do seaborn passando parâmetros: size e aspect. Por exemplo:

# In[5]:


# Plot não gradeado
plt.figure(figsize=(12,3))
sns.countplot(x='sex',data=tips)


# In[6]:


# Plot tipo grade
sns.lmplot(x='total_bill',y='tip',size=2,aspect=4,data=tips)


# ## Escala e Contexto
# 
# O set_context () permite que você substitua parâmetros padrão:

# In[7]:


sns.set_context('poster',font_scale=4)
sns.countplot(x='sex',data=tips,palette='coolwarm')


# Confira a página de documentação para obter mais informações sobre esses tópicos:
# https://stanford.edu/~mwaskom/software/seaborn/tutorial/aesthetics.html

# In[8]:


sns.puppyplot()

