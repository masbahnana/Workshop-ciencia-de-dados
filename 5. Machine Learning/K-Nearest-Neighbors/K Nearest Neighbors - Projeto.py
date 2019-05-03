#!/usr/bin/env python
# coding: utf-8

# # K Nearest Neighbors - Projeto 
# 
# Bem-vindo ao Projeto de KNN! Este será um projeto simples e muito parecido com o notebook, com a diferença de que você receberá outro conjunto de dados. Vá em frente e siga as instruções abaixo.
# ## Importar bibliotecas
# ** Importe pandas, seaborn e as bibliotecas usuais. **

# In[1]:





# ## Obtenha os dados
# ** Leia o arquivo csv 'KNN_Project_Data' em um DataFrame **

# In[2]:





# ** Verifique o cabeçalho do DataFrame.**

# In[23]:





# # Análise exploratória de dados
# 
# Uma vez que esses dados são artificiais, vamos criar um grande pairplot com o Seaborn.
# 
# ** Use seaborn no DataFrame para criar um pairplot com a tonalidade indicada pela coluna TARGET CLASS. **

# In[4]:





# # Padronize as variáveis
# 
# Hora de para padronizar as variáveis.
# 
# ** Import StandardScaler do Scikit-learn. **

# In[5]:





# ** Crie um objeto StandardScaler() chamado scaler. **

# In[6]:





# ** Use o método fit() do objeto para treinar o modelo. **

# In[7]:





# ** Use o método .transform () para transformar os parâmetros em uma versão padronizada. **

# In[8]:





# ** Converta os parâmetros padronizados em um DataFrame e verifique o cabeçalho desse DataFrame para garantir que a transform() funcionou. **

# In[9]:





# # Divisão treino-teste
# 
# ** Use o método train_test_split para dividir seus dados em um conjunto treino e teste.**

# In[10]:





# In[11]:





# # Usando o KNN
# 
# ** Importe o KNeighborClassifier do scikit learn. **

# In[12]:





# ** Crie uma instância do modelo KNN com n_neighbors = 1 **

# In[13]:





# ** Ajuste este modelo KNN aos dados de treinamento. **

# In[14]:





# # Previsões e avaliações
# Vamos avaliar o nosso modelo KNN!

# ** Use o método de previsão para prever valores usando seu modelo KNN e X_test. **

# In[24]:





# ** Crie uma matriz de confusão e um relatório de classificação. **

# In[16]:





# In[17]:





# In[18]:





# # Escolhendo o valor K
# Vamos continuar usando o método do cotovelo para escolher um bom valor K!
# 
# ** Crie um loop for que treine vários modelos KNN com valores k diferentes e, em seguida, mantenha um registro do error_rate para cada um desses modelos com uma lista. Consulte o notebook se você estiver confuso nesta etapa. **

# In[25]:





# ** Agora crie o seguinte gráfico usando as informações do seu loop. **

# In[20]:





# ## Treine seu modelo novamente com novo valor K
# 
# ** Treine novamente seu modelo com o melhor valor K (até você para decidir o que deseja) e re-faça o relatório de classificação e a matriz de confusão. **

# In[21]:




