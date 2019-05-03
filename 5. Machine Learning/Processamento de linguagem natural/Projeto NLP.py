#!/usr/bin/env python
# coding: utf-8

# # Projeto de processamento de linguagem natural
# 
# Bem-vindo ao Projeto NLP para esta seção do curso. Neste projeto NLP, você estará tentando classificar Avaliações da Yelp em categorias de 1 estrela ou 5 estrelas com base no conteúdo do texto nas revisões. Este será um procedimento mais simples do que a palestra, pois utilizaremos os métodos do pipeline para tarefas mais complexas.
# 
# Usaremos o [Conjunto de dados de reviews da Yelp da Kaggle](https://www.kaggle.com/c/yelp-recsys-2013).
# 
# Cada observação neste conjunto de dados é uma revisão de um determinado negócio por um determinado usuário.
# 
# A coluna "stars" é o número de estrelas (1 a 5) atribuídas pelo revisor ao negócio (mis estrelas é melhor.) 
# A coluna "cool" é o número de votos "legais" que esta avaliação recebeu de outros usuários de usuários.
# 
# Todas as avaliações começam com 0 votos "legais", e não há limite para quantos votos "legais" podem receber uma avaliação. Em outras palavras, é uma classificação da revisão em si, não uma classificação do negócio.
# 
# As colunas "useful" e "funny" são semelhantes à coluna "cool".
# 
# Vamos começar! Basta seguir as instruções abaixo!

#  ## Importações
#   ** Importe as bibliotecas habituais. **

# In[1]:


import numpy as np
import pandas as pd


# ## Os dados
# 
# ** Leia o arquivo yelp.csv e configure-o como um dataframe chamado yelp. **

# In[4]:


yelp = pd.read_csv("yelp.csv")


# ** Verifique os métodos head(), info() e describe() em yelp. **
# 

# In[5]:


yelp.head()


# In[6]:


yelp.info()


# In[7]:


yelp.describe()


# ** Crie uma nova coluna chamada "comprimento do texto", que é o número de palavras na coluna de texto. **

# In[9]:


yelp['text lenght'] = yelp['text'].apply(len)
yelp['text lenght'].head()


# # Análise exploratória de dados
# 
# Vamos explorar os dados
# 
# ## Importações
# 
# ** Importe as bibliotecas de visualização de dados se você ainda não o fez. **

# In[10]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
get_ipython().run_line_magic('matplotlib', 'inline')


# ** Use o FacetGrid da biblioteca seaborn para criar uma grid de 5 histogramas de comprimento de texto com base nas classificações das estrelas. Consulte a documentação Seaborn para obter dicas sobre como fazer isso, caso não lembre. **

# In[13]:


g = sns.FacetGrid(yelp, col='stars')
g.map(plt.hist, 'text lenght', bins=20)


# ** Crie um boxplot do comprimento de texto para cada categoria de estrelas. **

# In[14]:


sns.boxplot(x='stars', y='text lenght', data=yelp)


# ** Crie um countplot do número de ocorrências para cada tipo de classificação de estrelas. **

# In[15]:


sns.countplot(x='stars', data=yelp, palette='rainbow')


# ** Use groupby para obter os valores médios das colunas numéricas. **

# In[16]:


stars = yelp.groupby('stars').mean()
stars


# ** Use o método corr () nesse conjunto de dados groupby para produzir este dataframe: **

# In[17]:


stars.corr()


# ** Em seguida, use Seaborn para criar um heatmap com base em que .corr () dataframe: **

# In[19]:


sns.heatmap(stars.corr(), cmap='coolwarm', annot=True)


# ## Tarefa de classificação de PNL
# 
# Vamos passar para a tarefa atual. Para tornar as coisas um pouco mais fáceis, vá em frente e apenas pegue comentários que foram de 1 estrela ou 5 estrelas.
# 
# ** Crie um banco de dados chamado yelp_class que contenha as colunas do banco de dados do yelp, mas apenas para as avaliações de 1 ou 5 estrelas. **

# In[21]:


yelp_class = yelp[(yelp.stars==1) | (yelp.stars==5)]
yelp_class.stars.value_counts()


# ** Crie dois objetos X e y. X será a coluna "texto" de yelp_class e y será a coluna 'estrelas' do yelp_class.**

# In[22]:


X = yelp_class['text']
y = yelp_class['stars']


# ** Import CountVectorizer e crie um objeto CountVectorizer. **

# In[23]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()


# ** Use o método fit_transform no objeto CountVectorizer e passe em X (a coluna 'texto'). Salve esse resultado substituindo X. **

# In[24]:


X = cv.fit_transform(X)


# ## Divisão treino-teste
# 
# Vamos dividir nossos dados em dados de treinamento e teste.
# 
# ** Use train_test_split para dividir os dados em X_train, X_test, y_train, y_test. Use test_size = 0.3 e random_state = 101 **

# In[25]:


from sklearn.model_selection import train_test_split


# In[26]:


X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3,random_state=101)


# ## Training a Model
# 
# Tempo para treinar o modelo!
# 
# ** Import MultinomialNB e crie uma instância do estimador e o chame de nb **

# In[27]:


from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()


# ** Agora ajuste nb usando os dados de treinamento. **

# In[29]:


nb.fit(X_train, y_train)


# ## Previsões e avaliações
# 
# Tempo para ver como nosso modelo ficou!
# 
# ** Use o método predict() do nb para prever X_test. **

# In[30]:


pred = nb.predict(X_test)


# ** Crie uma matriz de confusão e um relatório de classificação usando essas previsões e y_test **

# In[31]:


from sklearn.metrics import classification_report, confusion_matrix


# In[32]:


print(confusion_matrix(y_test, pred))
print('\n')
print(classification_report(y_test, pred))


# **Ótimo! Vamos ver o que acontece se tentarmos incluir o TF-IDF nesse processo usando um pipeline. **

# # Usando o processamento de texto
# 
# ** Importe TfidfTransformer do sklearn. **

# In[33]:


from sklearn.feature_extraction.text import TfidfTransformer


# ** Importe pipeline da sklearn. **

# In[36]:


from sklearn.pipeline import Pipeline


# ** Agora crie um pipeline com as seguintes etapas: CountVectorizer (), TfidfTransformer (), MultinomialNB () **

# In[37]:


pipeline = Pipeline([
    ('bow', CountVectorizer()),
    ('tdidf', TfidfTransformer()),
    ('classifier', MultinomialNB()),
])


# ## Using the Pipeline
# 
# ** Hora de usar o pipeline! Lembre-se de que este pipeline já possui todas as suas etapas de pré-processo, o que significa que precisaremos re-dividir os dados originais (Lembre-se de que sobrecarregamos o X como a versão CountVectorized. O que precisamos é apenas o texto **

# ### Divisão treino-teste
# 
# ** Refaça a divisão treino-teste no objeto yelp_class. **

# In[38]:


X = yelp_class['text']
y = yelp_class['stars']
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3,random_state=101)


# ** Agora ajuste o pipeline aos dados de treinamento. Lembre-se de que você não pode usar os mesmos dados de treinamento da última vez porque esses dados já foram vetados. Precisamos passar apenas no texto e nos rótulos **

# In[39]:


pipeline.fit(X_train, y_train)


# ### Previsões e Avaliação
# 
# ** Agora use o pipeline para prever a partir do X_test e crie um relatório de classificação e uma matriz de confusão. Você deve notar resultados estranhos. **

# In[40]:


pred = pipeline.predict(X_test)


# In[41]:


print(confusion_matrix(y_test, pred))
print('\n')
print(classification_report(y_test, pred))


# Parece que o Tf-Idf realmente piorou as coisas!
# 
# É isto para este projeto. 
# ** Algumas outras coisas para tentar .... **
# Tente voltar e brincar com as etapas do pipeline e ver se criar um analisador personalizado como fizemos na aula... Ou recrie o pipeline com apenas o CountVectorizer() e NaiveBayes. A mudança do modelo ML no final para outro classificador ajudou?

# In[ ]:




