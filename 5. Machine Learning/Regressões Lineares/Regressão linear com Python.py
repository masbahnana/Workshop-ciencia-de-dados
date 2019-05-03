#!/usr/bin/env python
# coding: utf-8

# # Regressão linear com Python
# 
# 
# ** Este é apenas um código para referência. Por favor, veja as conferências de video para mais informações por trás de todo esse código. **
# 
# Seu vizinho é um agente imobiliário e quer alguma ajuda a prever os preços das casas para as regiões nos EUA. Seria ótimo se você pudesse de alguma forma criar um modelo para ela que lhe permita colocar algumas características de uma casa e retornar uma estimativa de quanto a casa venderia.
# 
# Ela perguntou se você poderia ajudá-la com suas novas habilidades de ciência de dados. Você diz sim e decide que a Regressão linear pode ser um bom caminho para resolver esse problema.
# 
# Seu vizinho, em seguida, dá-lhe algumas informações sobre um monte de casas em regiões dos Estados Unidos. tudo está contido no arquivo: USA_Housing.csv.
# 
# Os dados contém as seguintes colunas:
# 
# * 'Avg. Area Income': Média da renda dos residentes de onde a casa está localizada.
# * 'Avg. Area House Age': Média de idade das casas da mesma cidade.
# * 'Avg. Area Number of Rooms': Número médio de quartos para casas na mesma cidade.
# * 'Avg. Area Number of Bedrooms': Número médio de quartos para casas na mesma cidade
# * 'Area Population': A população da cidade onde a casa está localizada.
# * 'Price': Preço de venda da casa.
# * 'Address': Endereço da casa;

# **Vamos começar!**
# ## Confira os dados
# Nós conseguimos obter alguns dados do seu vizinho para os preços da habitação como um conjunto de csv, vamos preparar nosso ambiente com as bibliotecas que precisaremos e depois importar os dados!
# ### Importar bibliotecas

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Confira os dados

# In[2]:


USAhousing = pd.read_csv('USA_Housing.csv')


# In[3]:


USAhousing.head()


# In[4]:


USAhousing.info()


# In[5]:


USAhousing.describe()


# In[260]:


USAhousing.columns


# # EDA
# 
# Vamos criar alguns plots simples para verificar os dados.

# In[6]:


sns.pairplot(USAhousing)


# In[8]:


sns.distplot(USAhousing['Price'])


# In[9]:


sns.heatmap(USAhousing.corr())


# ## Treinando um modelo de regressão linear
# 
# Vamos agora começar a treinar o modelo de regressão. Precisamos primeiro dividir nossos dados em uma matriz X que contém os recursos para treinar, e uma matriz y com a variável alvo, neste caso, a coluna Preço. Vamos descartar a coluna "Adress" porque só tem informações de texto que o modelo de regressão linear não pode usar.
# 
# ### Arrays X e y

# In[10]:


X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAhousing['Price']


# ## Split de treino
# 
# Agora vamos dividir os dados em um conjunto de treinamento e um conjunto de testes. Vamos criar o modelo usando o conjunto de treinamento e depois usar o conjunto de testes para avaliar o modelo.

# In[11]:


from sklearn.model_selection import train_test_split


# In[12]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)


# ## Criando e treinando o modelo

# In[13]:


from sklearn.linear_model import LinearRegression


# In[14]:


lm = LinearRegression()


# In[15]:


lm.fit(X_train,y_train)


# ## Avaliação modelo
# 
# Vamos avaliar o modelo ao verificar os coeficientes e como podemos interpretá-los.

# In[16]:


# Printando a intercepção
print(lm.intercept_)


# In[17]:


coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
coeff_df


# Interpretando os coeficientes:
# 
# - Mantendo todas as outras variáveis constantes, um aumento de 1 unidade em ** Avg. Area Income ** está associado a um **aumento de \$ 21,52**.
# - Mantendo todas as outras variáveis constantes, um aumento de 1 unidade em ** Avg. Area House Age ** está associada a um ** aumento de \$ 164883.28 **.
# - Mantendo todas as outras variáveis constantes, um aumento de 1 unidade em ** Avg. Area Number of Bedrooms ** está associada a um ** aumento de \$ 122368.67 **.
# - Mantendo todas as outras variáveis constantes, um aumento de 1 unidade em ** Avg. Area Number of Bedrooms ** está associada a um ** aumento de \$ 2233.80 **.
# - Mantendo todas as outras variáveis constantes, um aumento de 1 unidade em ** Area Population ** está associado a um ** aumento de \$ 15.15 **.
# 
# Isso faz sentido? Provavelmente não porque esses dados não são reais. Se quiser dados reais para repetir este tipo de análise, confira o [conjunto de dados de Boston](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html):
# 

#     from sklearn.datasets import load_boston
#     boston = load_boston()
#     print(boston.DESCR)
#     boston_df = boston.data

# ## Predições do nosso modelo
# 
# Vamos pegar as previsões em nosso conjunto de testes e ver o quão bem!

# In[18]:


predictions = lm.predict(X_test)


# In[19]:


plt.scatter(y_test,predictions)


# **Histograma residual**

# In[20]:


sns.distplot((y_test-predictions),bins=50);


# ## Métricas de avaliação de regressão
# 
# 
# Aqui estão três métricas de avaliação comuns para problemas de regressão:
# 
# **Mean absolute error ** (erro absoluto médio) (MAE) é a média do valor absoluto dos erros:
# 
# $$\frac 1n\sum_{i=1}^n|y_i-\hat{y}_i|$$
# 
# ** Mean Squared Error ** (erro médio quadrático) (MSE) é a média dos erros quadrados:
# 
# $$\frac 1n\sum_{i=1}^n(y_i-\hat{y}_i)^2$$
# 
# ** Root Mean Square Error ** (raiz do erro quadrático médio) (RMSE) é a raiz quadrada da média dos erros quadrados:
# 
# $$\sqrt{\frac 1n\sum_{i=1}^n(y_i-\hat{y}_i)^2}$$
# 
# Comparando estas métricas:
# 
# - **MAE** é o mais fácil de entender, porque é o erro médio.
# - **MSE** é mais popular que o MAE, porque a MSE "puniria" erros maiores, o que tende a ser útil no mundo real.
# - **RMSE** é ainda mais popular do que MSE, porque o RMSE é interpretável nas unidades "y".
# 
# Todas estas são ** funções de perda **, porque queremos minimizá-las.

# In[21]:


from sklearn import metrics


# In[22]:


print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))


# Este foi o seu primeiro projeto de Machine Learning real! Parabéns em ajudar o seu vizinho! Vamos deixar isso terminar aqui por enquanto, mas vá em frente e explore o Dataset de Boston mencionado anteriormente se este conjunto de dados específico for interessante para você!
# 
# A seguir, o seu próprio Projeto de Machine Learning!
