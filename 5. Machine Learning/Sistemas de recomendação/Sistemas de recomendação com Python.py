#!/usr/bin/env python
# coding: utf-8

# # Sistemas de recomendação com Python
# 
# Bem-vindo ao notebook de Sistemas de recomendação com o Python. Nesta palestra, discutiremos sobre sistemas básicos de recomendação usando Python e pandas. Há outro notebook: * Sistemas avançados de recomendação com Python*. Esse notebook é mais detalhado, porém, com o mesmo conjunto de dados.
# 
# Neste notebook nos concentraremos em fornecer um sistema de recomendação básico, sugerindo itens que são mais parecidos com um item específico, neste caso, filmes. Tenha em mente que este não é um verdadeiro sistema de recomendação robusto, para descrevê-lo com mais precisão, apenas diz o que os filmes / itens são mais parecidos com a escolha do seu filme.
# 
# Não há nenhum projeto para este tópico, em vez disso você tem a opção de trabalhar com a versão de conferência avançada deste notebook (totalmente opcional!).
# 
# Vamos começar!
# 
# ## Importar bibliotecas

# In[2]:


import numpy as np
import pandas as pd


# ## Obter os dados

# In[3]:


column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data', sep='\t', names=column_names)


# In[4]:


df.head()


# Agora vamos receber os títulos do filme:

# In[5]:


movie_titles = pd.read_csv("Movie_Id_Titles")
movie_titles.head()


# Podemos juntá-los:

# In[6]:


df = pd.merge(df,movie_titles,on='item_id')
df.head()


# # Análise exploratória de dados
# 
# Vamos explorar os dados um pouco e dê uma olhada em alguns dos filmes mais bem classificados.
# 
# ## Visualização Importações

# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
get_ipython().run_line_magic('matplotlib', 'inline')


# Vamos criar um dataframes de ratings com classificação média e número de avaliações:

# In[8]:


df.groupby('title')['rating'].mean().sort_values(ascending=False).head()


# In[9]:


df.groupby('title')['rating'].count().sort_values(ascending=False).head()


# In[10]:


ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings.head()


# Agora, defina a coluna de número de classificações:

# In[11]:


ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()


# E alguns histogramas:

# In[146]:


plt.figure(figsize=(10,4))
ratings['num of ratings'].hist(bins=70)


# In[147]:


plt.figure(figsize=(10,4))
ratings['rating'].hist(bins=70)


# In[148]:


sns.jointplot(x='rating',y='num of ratings',data=ratings,alpha=0.5)


# OK! Agora que temos uma idéia geral de como os dados se parecem, vamos passar para a criação de um sistema de recomendação simples:

# ## Recomendando filmes semelhantes

# Agora vamos criar uma matriz que tenha o ID dos usuários em um acesso e o título do filme em outro eixo. Cada célula irá consistir na classificação que o usuário deu a esse filme. Observe que haverá muitos valores de NaN, porque a maioria das pessoas não viu a maioria dos filmes.

# In[149]:


moviemat = df.pivot_table(index='user_id',columns='title',values='rating')
moviemat.head()


# Filme mais avaliado:

# In[150]:


ratings.sort_values('num of ratings',ascending=False).head(10)


# Vamos escolher dois filmes: starwars, um filme de ficção científica e Liar Liar, uma comédia.

# In[161]:


ratings.head()


# Agora vamos pegar as avaliações dos usuários para esses dois filmes:

# In[162]:


starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']
starwars_user_ratings.head()


# Podemos então usar o método corrwith() para obter correlações entre duas séries de pandas:

# In[163]:


similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)


# Vamos limpar isso removendo valores de NaN e usando um DataFrame em vez de uma série:

# In[164]:


corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head()


# Agora, se classificarmos o quadro de dados por correlação, devemos obter os filmes mais parecidos, no entanto, notemos que obtemos alguns resultados que realmente não fazem sentido. Isso ocorre porque há muitos filmes apenas assistidos uma vez por usuários que também assistiram a star wars (foi o filme mais popular).

# In[155]:


corr_starwars.sort_values('Correlation',ascending=False).head(10)


# Vamos corrigir isso, filtrando filmes com menos de 100 comentários (esse valor foi escolhido com base no histograma anterior).

# In[165]:


corr_starwars = corr_starwars.join(ratings['num of ratings'])
corr_starwars.head()


# Agora, classifique os valores e observe como os títulos têm muito mais sentido:

# In[157]:


corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation',ascending=False).head()


# Agora o mesmo para Liar Liar:

# In[158]:


corr_liarliar = pd.DataFrame(similar_to_liarliar,columns=['Correlation'])
corr_liarliar.dropna(inplace=True)
corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation',ascending=False).head()

