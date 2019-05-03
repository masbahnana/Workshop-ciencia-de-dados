#!/usr/bin/env python
# coding: utf-8

# # Projeto de Regressão Logística
# 
# 
# Neste projeto estaremos trabalhando com um conjunto de dados falso de publicidade, indicando se um usuário de internet específico clicou ou não em uma propaganda. Vamos tentar criar um modelo que preveja se clicará ou não em um anúncio baseado nos recursos desse usuário.
# 
# Este conjunto de dados contém os seguintes recursos:
# 
# * 'Daily Time Spent on Site': tempo no site em minutos.
# * 'Age': idade do consumidor.
# * 'Area Income': Média da renda do consumidor na região.
# * 'Daily Internet Usage': Média em minutos por di que o consumidor está na internet.
# * 'Linha do tópico do anúncio': Título do anúncio.
# * 'City': Cidade do consumidor.
# * 'Male': Se o consumidor era ou não masculino.
# * 'Country': País do consumidor.
# * 'Timestamp': hora em que o consumidor clicou no anúncio ou janela fechada.
# * 'Clicked on Ad'': 0 ou 1 indicam se clicou ou não no anúncio.
# 
# ## Importar bibliotecas
# 
# ** Importe algumas bibliotecas que você acha que você precisará **

# In[1]:





# ## Obter dados
# ** Leia o arquivo advertising.csv e grave-o em um DataFrame chamado ad_data. **

# In[4]:





# ** Verifique o cabeçalho do ad_data **

# In[5]:





# ** Use info() e describe() em ad_data **

# In[6]:





# In[42]:





# ## Análise de dados exploratória
# 
# Vamos usar Seaborn para explorar os dados!
# 
# Tente recriar os gráficos abaixo.
# 
# ** Crie um histograma de "Age" **

# In[48]:





# ** Crie um joinplot mostrando "Area Income" versus "Age" **

# In[64]:





# ** Crie um jointplot que mostre as distribuições KDE do "Daily Time spent" no site vs "Age". **

# In[66]:





# ** Crie um jointplot do 'Daily Time Spent on Site' vs. 'Daily Internet Usage'**

# In[72]:





# ** Finalmente, crie um parplot com o matiz definido pelo recurso de coluna 'Clicked on Ad'. **

# In[84]:





# 
# # Regressão Logística
# 
# Agora é hora de quebrar nossos dados em treino e teste e fitar nosso modelo.
# 
# Você terá a liberdade aqui para escolher colunas em que deseja treinar!

# ** Divida os dados em conjunto de treinamento e conjunto de testes usando train_test_split **

# In[85]:





# In[88]:





# In[89]:





# ** Treine e ajuste um modelo de regressão logística no conjunto de treinamento. **

# In[91]:





# In[92]:





# ## Previsões e avaliações
# ** Agora preveja valores para os dados de teste. **

# In[94]:





# ** Crie um relatório de classificação para o modelo. **

# In[95]:





# In[96]:




