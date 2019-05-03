#!/usr/bin/env python
# coding: utf-8

# # Regressão Linear - Projeto
# 
# Parabéns! Você obteve algum contrato de trabalho com uma empresa de comércio eletrônico com sede na cidade de Nova York que vende roupas online, mas também tem sessões de consultoria em estilo e vestuário na loja. Os clientes entram na loja, têm sessões / reuniões com um estilista pessoal, então podem ir para casa e encomendarem em um aplicativo móvel ou site para a roupa que desejam.
# 
# A empresa está tentando decidir se deve concentrar seus esforços em sua experiência em aplicativos móveis ou em seu site. Eles contrataram você no contrato para ajudá-los a descobrir isso! Vamos começar!
# 
# Basta seguir as etapas abaixo para analisar os dados do cliente (é falso, não se preocupe, eu não lhe dei números reais de cartões de crédito ou e-mails).

# ## Imports
# ** Importe pandas, numpy, matplotlib,e seaborn. Em seguida, configure% matplotlib inline
# (Você importará sklearn conforme você precisar). **

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# ## Obter dados
# 
# Trabalharemos com o arquivo csv do Ecommerce Customers da empresa. Possui informações do cliente, como Email, Endereço e sua cor Avatar. Em seguida, ele também possui colunas de valores numéricos:.
# 
# * Avg. Session Length: Tempo médio das sessões de consultoria de estilo na loja.
# * Time on App: tempo médio gasto no app em minutos.
# * Time on Website: tempo médio gasto no site em minutos.
# * Lenght of Membership: Há quantos anos o cliente é membro.
# 
# ** Leia no arquivo csv do Ecommerce Customers como um DataFrame chamado clientes. **

# In[2]:


clientes = pd.read_csv("Ecommerce Customers")


# ** Verifique o cabeçalho dos clientes e confira os seus métodos info () e describe(). **

# In[3]:


clientes.head()


# In[4]:


clientes.describe()


# In[5]:


clientes.info()


# ## Análise de dados exploratória
# 
# ** Vamos explorar os dados! **
# 
# Pelo resto do exercício, só estaremos usando os dados numéricos do arquivo csv.
# ___
# ** Use seaborn para criar um jointplot para comparar as colunas Time On Website e Volume anual. A correlação faz sentido? **

# In[6]:


sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=clientes)


# In[281]:





# ** Faça o mesmo, mas com a coluna tempo no aplicativo (Time on App), em vez disso. **

# In[7]:


sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=clientes)


# ** Use jointplot criar um lote de caixa hexagonal 2D que compara tempo no aplicativo (Time on App) e o tempo da associação (Length of Membership). **

# In[8]:


sns.jointplot(x='Time on App', y='Length of Membership', data=clientes, kind='hex')


# ** Vamos explorar esses tipos de relações em todo o conjunto de dados. Use [parplot](https://stanford.edu/~mwaskom/software/seaborn/tutorial/axis_grids.html#plotting-pairwise-relationships-with-pairgrid-and-pairplot) para recriar o gráfico abaixo. (Não se preocupe com as cores) **

# In[9]:


sns.pairplot(clientes)


# ** Baseado neste plot o que parece ser a característica mais correlacionada com o valor anual gasto (Yearly Amount Spent)? **

# In[285]:





# ** Crie um plot de um modelo linear (usando o lmplot de Seaborn) da quantia anual gasta (Yearly Amount Spent) vs. tempo de associação (Length of Membership). **

# In[11]:


sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=clientes)


# ## Treinando e testando os dados
# 
# Agora que exploramos um pouco os dados, vamos avançar e dividir os dados em conjuntos de treinamento e teste.
# ** Defina uma variável X igual a todas as características numéricas dos clientes e uma variável y igual à coluna Valor anual gasto (Yearly Amount Spent). **

# In[12]:


y = clientes['Yearly Amount Spent']


# In[13]:


X= clientes[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]


# ** Use model_selection.train_test_split da sklearn para dividir os dados em conjuntos de treinamento e teste. Defina test_size = 0.3 e random_state = 101 **

# In[16]:


from sklearn.model_selection import train_test_split


# In[17]:


X_train, X_test, y_train,y_test =train_test_split(X, y, test_size=0.3,random_state=101)


# ## Treinando o modelo
# 
# Agora é hora de treinar nosso modelo em nossos dados de treinamento!
# 
# ** Importe LinearRegression do sklearn.linear_model **

# In[18]:


from sklearn.linear_model import LinearRegression


# ** Crie uma instância de um modelo LinearRegression () chamado lm. **

# In[19]:


lm = LinearRegression()


# ** Treine lm nos dados de treinamento. **

# In[21]:


lm.fit(X_train, y_train)


# **Print os coeficientes do modelo**

# In[22]:


lm.coef_


# ## Previsão de dados de teste
# Agora que nos ajustamos ao nosso modelo, vamos avaliar o seu desempenho ao prever os valores de teste!
# 
# ** Use lm.predict () para prever o conjunto X_test dos dados. **

# In[23]:


prediction = lm.predict(X_test)


# ** Crie um diagrama de dispersão (scatterplot) dos valores reais de teste em relação aos valores preditos. **

# In[24]:


plt.scatter(y_test, prediction)
plt.xlabel('Y test')
plt.ylabel('Predicted Y')


# ## Avaliando o Modelo
# 
# Vamos avaliar o desempenho do nosso modelo calculando a soma residual dos quadrados e o escore de variância explicado (R ^ 2).
# 
# ** Calcule o erro absoluto médio, o erro quadrado médio e o erro quadrado médio da raiz. Consulte a palestra ou a Wikipédia para as fórmulas **

# In[26]:


from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(y_test, prediction))
print('MSE:', metrics.mean_squared_error(y_test, prediction))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, prediction)))


# ## Resíduos
# 
# Você deve ter obtido um modelo muito bom com um bom ajuste. Vamos explorar rapidamente os resíduos para garantir que tudo esteja bem com os nossos dados.
# 
# ** Trace um histograma dos resíduos e certifique-se de que ele parece normalmente distribuído. Use o seaborn distplot, ou apenas o plt.hist (). **

# In[28]:


sns.distplot((y_test-prediction), bins=50)


# ## Conclusão
# Ainda desejamos descobrir a resposta à pergunta original, concentramos-nos no desenvolvimento de aplicativos móveis ou de sites? Ou talvez isso realmente não importe, e o tempo como membro é o que é realmente importante? Vamos ver se podemos interpretar os coeficientes para ter uma idéia.
# 
# ** Recrie o quadro de dados abaixo. **

# In[29]:


coef = pd.DataFrame(lm.coef_, X.columns, columns=['Coefs'])
coef


# ** Como você pode interpretar esses coeficientes? **

# 

# ** Você acha que a empresa deve se concentrar mais em seu aplicativo móvel ou em seu site? **

# 
