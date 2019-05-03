#!/usr/bin/env python
# coding: utf-8

# # Projeto de dados do mercado financeiro
# 
# Neste projeto de dados, nos concentraremos na análise de dados exploratórios dos preços das ações. Tenha em mente que este projeto apenas pretende praticar suas habilidades de visualização e pandas, não é para ser uma análise financeira robusta ou ser tomado como um conselho financeiro.
# ____
# ** NOTA: Este projeto é extremamente desafiador, porque irá introduzir muitos novos conceitos e te fará procurar as coisas por conta própria (vamos apontar você na direção certa) para tentar resolver as tarefas emitidas. Sinta-se à vontade para passar pelo livro de conferências de soluções e no vídeo como um projeto "passo a passo" se você não quer ter que procurar as coisas sozinho. Você ainda aprenderá muito dessa forma! **
# ____
# Vamos nos concentrar nas ações dos banco e ver como eles performaram durante a [crise financeira](https://en.wikipedia.org/wiki/Financial_crisis_of_2007%E2%80%9308) até o início de 2016.

# ## Obter dados
# 
# Nesta seção, aprenderemos a usar pandas para ler diretamente os dados das finanças do Google usando pandas!
# 
# Primeiro, precisamos começar com as importações adequadas, que já apresentamos para você aqui.
# 
# * Nota: [Você precisará instalar pandas-datareader para que isso funcione!](Https://github.com/pydata/pandas-datareader) O datareader Pandas permite que você [leia informações das ações diretamente da internet](http : //pandas.pydata.org/pandas-docs/stable/remote_data.html) Use estes links para orientação de instalação (** pip install pandas-datareader **), ou simplesmente acompanhe a conferência de vídeo. *
# 
# ### Os Imports
# 
# Já preenchidos para você.

# In[4]:


from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Dados
# 
# Precisamos obter dados usando o datareader de pandas. Obteremos informações sobre ações para os seguintes bancos:
# * Bank of America
# * CitiGroup
# * Goldman Sachs
# * JPMorgan Chase
# * Morgan Stanley
# * Wells Fargo
# 
# ** Descubra como obter os dados de ações de 1 de janeiro de 2006 a 1º de janeiro de 2016 para cada um desses bancos. Defina cada banco como um dataframe separado, com o nome da variável para que esse banco seja seu símbolo de ticker. Isso envolverá algumas etapas: **
# 1. Use datetime para definir objetos de início e fim de data e hora.
# 2. Descobrir o símbolo do ticker para cada banco.
# 2. Descubra como usar o datareader para pegar as cotações.
# 
# ** Use [esta página de documentação](http://pandas.pydata.org/pandas-docs/stable/remote_data.html) para obter dicas e instruções. Use o google finance como um fonte, por exemplo: **
#     
#      # Banco da América
#      BAC = data.DataReader ("BAC", "google", início e fim)
# 

# In[5]:





# In[6]:





# In[50]:





# ** Crie uma lista dos símbolos dos tickers (como strings) em ordem alfabética. Chame esta lista: tickers **

# In[7]:





# ** Use pd.concat para concatenar os DataFrames do banco juntos em um único chamado bank_stocks. Defina o argumento das chaves igual à lista de tickers. Também preste atenção em que eixo você concatena. **

# In[8]:





# ** Defina os níveis dos nomes das colunas (este é preenchido para você): **

# In[9]:


bank_stocks.columns.names = ['Bank Ticker','Stock Info']


# ** Verifique o cabeçalho do DataFrame bank_stocks. **

# In[20]:





# # Análise de dados exploratória
# 
# Vamos explorar os dados um pouco! Antes de prosseguir, sugiro que você verifique a documentação no [Multi-Level Indexing](http://pandas.pydata.org/pandas-docs/stable/advanced.html) e [como usar .xs](http: // pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.xs.html).
# Consulte as soluções se você não consiga descobrir como usar .xs (), uma vez que isso será uma parte importante desse projeto.
# 
# ** Qual é o preço máximo de fechamento para cada banco durante todo o período? **

# In[58]:





# ** Crie um novo DataFrame vazio chamado returns. Este dataframe conterá os retornos para o ação de cada banco. Os retornos geralmente são definidos por: **
# 
# $$r_t = \frac{p_t - p_{t-1}}{p_{t-1}} = \frac{p_t}{p_{t-1}} - 1$$

# In[60]:





# ** Podemos usar o método pct_change () pandas na coluna close para criar uma coluna que represente esse valor de retorno. Crie um loop for que vá e para cada Bank Stock Ticker cria essa coluna de retorno e configura-a como uma coluna nos dados DataFrame. **

# In[65]:





# ** Crie um parplot utilizando seaborn no dataframe de retorno. **

# In[68]:





# ** Usando o seu DataFrame returns, descubra quais datas cada ação dos bancos teve o melhor e o pior dia de retorno. Você deve notar que 4 dos bancos compartilham o mesmo dia para a pior queda. Alguma coisa significante aconteceu naquele dia? **

# In[75]:





# In[76]:





# ** Dê uma olhada no desvio padrão dos retornos. Qual ação você classificaria como a mais arriscada durante todo o período de tempo? Qual você classificaria como a mais arriscado para o ano 2015? **

# In[81]:





# In[88]:





# ** Crie um distplot usando seaborn dos retornos de 2015 para Morgan Stanley **

# In[94]:





# ** Crie um distplot usando seaborn dos retornos de 2008 para CitiGroup **

# In[98]:





# # Mais visualização
# 
# Muito desse projeto se concentrará em visualizações. Sinta-se livre para usar qualquer uma das suas bibliotecas de visualização preferidas para tentar recriar os plots descritos abaixo, seaborn, matplotlib, plotly e cufflinks, ou apenas pandas.
# 
# ### Importações

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# ** Crie um gráfico de linha mostrando o preço de fechamento para cada banco para todo o índice de tempo. (Sugestão: tente usar um loop for ou use [.xs](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.xs.html) para obter uma seção transversal dos dados .) **

# In[17]:





# In[18]:





# ## Médias móveis
# 
# Vamos analisar as médias móveis para essas ações no ano de 2008.
# 
# ** Trace a média de 30 dias para o preço do Bank Of America para o ano de 2008 **

# In[141]:





# ** Crie um mapa de calor da correlação entre os preços de fechamento das ações. **

# In[41]:





# ** Opcional: use o clustermap do seaborn para agrupar as correlações: **

# In[26]:





# Definitivamente, muitos tópicos de finanças específicos aqui, então não se preocupe se você não os entendeu todos! A única coisa que você deve estar preocupado com a compreensão são os pandas básicos e operações de visualização.
