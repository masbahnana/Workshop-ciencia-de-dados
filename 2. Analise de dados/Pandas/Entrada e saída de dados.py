#!/usr/bin/env python
# coding: utf-8

# # Entrada e saída de dados
# 
# Este notebook conterá nossas referências sobre entrada e saída de dados. O pandas pode ler uma variedade de tipos de arquivos usando seus métodos pd.read_. Vejamos os tipos de dados mais comuns:

# In[1]:


import numpy as np
import pandas as pd


# ## CSV
# 
# ### CSV Input

# In[2]:


df = pd.read_csv('exemplo')
df


# ### Saída de dados tipo CSV 

# In[3]:


df.to_csv('exemplo.csv',index=False)


# ## Excel
# 
# Pandas podem ler e escrever arquivos do Excel, tenha em mente, isso só importa dados. Não fórmulas nem imagens, lembrando que imagens ou macros podem bugar o método.

# ### Entrada via Excel

# In[4]:


pd.read_excel('Exemplo_Excel.xlsx',sheetname='Sheet1')


# ### Saída via Excel

# In[5]:


df.to_excel('Exemplo_Excel.xlsx',sheet_name='Sheet1')


# ## HTML
# 
# Você pode precisar instalar htmllib5, lxml e BeautifulSoup4. No seu terminal / prompt de comando, execute:
# 
#     conda install lxml
#     conda install html5lib
#     conda install BeautifulSoup4
#     
# Em seguida, reinicie o Jupyter Notebook. 
# (Ou use instalação de pip se não estiver usando a Distribuição de Anaconda)
# Pandas podem ler guias de tabelas fora de html. Por exemplo:

# ### Entrada HTML
# 
# A função Pandas read_html irá ler tabelas fora de uma página da Web e retornar uma lista de objetos DataFrame:

# In[10]:


df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')


# In[13]:


df[0]


# ____
