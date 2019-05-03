#!/usr/bin/env python
# coding: utf-8

# # K Nearest Neighbors com Python
# 
# Você recebeu um conjunto de dados classificados de uma empresa. Eles ocultaram a coluna de parâmetros, mas lhe deram os dados e a classe de destino.
# 
# Vamos tentar usar o KNN para criar um modelo que possa predizer diretamente a classe para um novo ponto de dados baseado nos parâmetros.
# 
# Vamos pegar e usá-lo!

# ## Import Libraries
# 
# 

# In[43]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Obter dados
# 
# Defina index_col = 0 para usar a primeira coluna como índice.

# In[74]:


df = pd.read_csv("Classified Data",index_col=0)


# In[75]:


df.head()


# ## Normalizar as variáveis
# 
# Como o classificador KNN prediz a classe de uma determinada observação ao identificar as observações mais próximas, a escala da variável é importante. Todas as variáveis que estão em grande escala terão um efeito muito maior na distância entre as observações e, portanto, sobre o classificador KNN, do que as variáveis em pequena escala.

# In[78]:


from sklearn.preprocessing import StandardScaler


# In[79]:


scaler = StandardScaler()


# In[80]:


scaler.fit(df.drop('TARGET CLASS',axis=1))


# In[81]:


scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))


# In[82]:


df_feat = pd.DataFrame(scaled_features,columns=df.columns[:-1])
df_feat.head()


# ## Divisão treino-teste

# In[83]:


from sklearn.model_selection import train_test_split


# In[84]:


X_train, X_test, y_train, y_test = train_test_split(scaled_features,df['TARGET CLASS'],
                                                    test_size=0.30)


# ## Usando o KNN
# 
# Lembre-se de que estamos tentando encontrar um modelo para prever se alguém estará na TARGET CLASS ou não. Começaremos com k = 1

# In[85]:


from sklearn.neighbors import KNeighborsClassifier


# In[86]:


knn = KNeighborsClassifier(n_neighbors=1)


# In[87]:


knn.fit(X_train,y_train)


# In[88]:


pred = knn.predict(X_test)


# ## Previsões e avaliações
# 
# Vamos avaliar o nosso modelo KNN!

# In[89]:


from sklearn.metrics import classification_report,confusion_matrix


# In[90]:


print(confusion_matrix(y_test,pred))


# In[91]:


print(classification_report(y_test,pred))


# # Escolhendo um valor K
# 
# Vamos em frente e usar o método do cotovelo para escolher um bom Valor K:

# In[ ]:


error_rate = []

# Levará algum tempo
for i in range(1,40):
    
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))


# In[99]:


plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')


# Aqui podemos ver que, após cerca de K > 23, a taxa de erro tende a girar em torno de 0,06-0,05. Vamos treinar novamente o modelo com isso e verificar o relatório de classificação!

# In[100]:


# PRIMEIRA COMPARAÇÃO RÁPIDA PARA O NOSSO ORIGINAL K = 1
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train,y_train)
pred = knn.predict(X_test)

print('WITH K=1')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))


# In[101]:


# Agora com K = 23
knn = KNeighborsClassifier(n_neighbors=23)

knn.fit(X_train,y_train)
pred = knn.predict(X_test)

print('WITH K=23')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))


# Conseguimos extrair mais algum desempenho do nosso modelo, ajustando-nos para um melhor valor K!
