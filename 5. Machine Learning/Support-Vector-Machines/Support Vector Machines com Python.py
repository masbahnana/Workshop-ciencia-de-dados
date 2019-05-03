#!/usr/bin/env python
# coding: utf-8

# # Support Vector Machines com Python
# 
# Bem vindo ao notebook sobre Support Vector Machines com Python! Lembre-se de se consultar o vídeo para obter informações completas sobre o código aqui!
# 
# ## Importando bibliotecas

# In[51]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Obter dados
# 
# Usaremos o conjunto de dados de câncer de mama incorporado da Scikit Learn. Podemos obter com a função load:

# In[52]:


from sklearn.datasets import load_breast_cancer


# In[54]:


cancer = load_breast_cancer()


# O conjunto de dados é apresentado em uma forma de dicionário:

# In[55]:


cancer.keys()


# Podemos pegar informações e arrays deste dicionário para configurar nosso dataframe e entender os recursos:

# In[4]:


print(cancer['DESCR'])


# In[56]:


cancer['feature_names']


# ## Configurando o DataFrame

# In[12]:


df_feat = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
df_feat.info()


# In[14]:


cancer['target']


# In[16]:


df_target = pd.DataFrame(cancer['target'],columns=['Cancer'])


# Agora vamos verificar o dataframe:

# In[8]:


df.head()


# # Análise de dados exploratórios

# Nós ignoraremos a parte Data Viz para esta leitura, pois existem tantos parâmetros que são difíceis de interpretar se você não tem conhecimento e domínio de câncer ou células tumorais. No seu projeto você terá mais oportunidades para visualizar os dados.

# ## Divisão treino-teste

# In[57]:


from sklearn.model_selection import train_test_split


# In[58]:


X_train, X_test, y_train, y_test = train_test_split(df_feat, np.ravel(df_target), test_size=0.30, random_state=101)


# # Treinando o Support Vector Classifier

# In[59]:


from sklearn.svm import SVC


# In[60]:


model = SVC()


# In[61]:


model.fit(X_train,y_train)


# ## Previsões e avaliações
# 
# Agora vamos prever o uso do modelo treinado.

# In[27]:


predictions = model.predict(X_test)


# In[45]:


from sklearn.metrics import classification_report,confusion_matrix


# In[46]:


print(confusion_matrix(y_test,predictions))


# In[62]:


print(classification_report(y_test,predictions))


# Note que estamos classificando tudo em uma única classe! Isso significa que nosso modelo precisa ter parâmetros ajustados (também pode ajudar a normalizar os dados).
# 
# Podemos procurar por parâmetros usando um GridSearch!

# # Gridsearch
# 
# Encontrar os parâmetros certos (como o que o C ou os valores de gama para usar) é uma tarefa complicada! Mas, felizmente, podemos ser um pouco preguiçosos e apenas tentar um monte de combinações e ver o que funciona melhor! Essa idéia de criar uma "grade" de parâmetros e apenas experimentar todas as combinações possíveis é chamada Gridsearch, esse método é comum o suficiente para que o Scikit-learn tenha essa funcionalidade incorporada no GridSearchCV!
# 
# O GridSearchCV usa um dicionário que descreve os parâmetros que devem ser testados e um modelo para treinar. A grade de parâmetros é definida como um dicionário, onde as chaves são os parâmetros e os valores são as configurações a serem testadas.

# In[63]:


param_grid = {'C': [0.1,1, 10, 100, 1000], 'gamma': [1,0.1,0.01,0.001,0.0001], 'kernel': ['rbf']} 


# In[64]:


from sklearn.model_selection import GridSearchCV


# Uma das grandes coisas do GridSearchCV é que é um meta-estimador. Ele pega um estimador como SVC e cria um novo estimador, que se comporta exatamente da mesma forma - neste caso, como um classificador. Você deve adicionar refit=True e escolher detalhadamente para  número desejado, maior o número, mais detalhado. 
# 
# Você deve adicionar refit=True e escolher  um número para o parâmetro verbose. Quanto maior o número, mais detalhamento teremos.

# In[65]:


grid = GridSearchCV(SVC(),param_grid,refit=True,verbose=3)


# O que o fit faz é um pouco mais complicado do que o habital. Primeiro, ele executa o mesmo loop com validação cruzada, para encontrar a melhor combinação de parâmetros. Uma vez que tenha a melhor combinação, ele corre novamente em todos os dados para fitá-los (sem validação cruzada), para construir um único modelo novo usando a melhor configuração de parâmetro.

# In[40]:


# Talvez demore um pouco
grid.fit(X_train,y_train)


# Você pode inspecionar os melhores parâmetros encontrados pelo GridSearchCV no atributo best_params_ e o melhor estimador no melhor atributo \ _estimator_:

# In[41]:


grid.best_params_


# In[ ]:


grid.best_estimator_


# Então você pode re-executar previsões neste objeto da grade exatamente como você faria com um modelo normal.

# In[48]:


grid_predictions = grid.predict(X_test)


# In[49]:


print(confusion_matrix(y_test,grid_predictions))


# In[50]:


print(classification_report(y_test,grid_predictions))

