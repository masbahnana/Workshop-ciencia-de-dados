#!/usr/bin/env python
# coding: utf-8

# # Exercício Mapas Choropleth  
# 
# Bem-vindo aos exercícios sobre mapas do Choropleth! Neste exercício, daremos alguns conjuntos de dados simples e pedimos que você crie o mapa a partir deles. Devido à natureza do Plotly, não podemos mostrar exemplos
# 
# [Documentação](https://plot.ly/python/reference/#choropleth)
# 
# ## Imports Plotly 

# In[1]:


import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=True) 


# ** Importe pandas e leia o arquivo csv: 2014_World_Power_Consumption **

# In[1]:





# In[152]:





# ** Verifique o cabeçalho do DataFrame. **

# In[156]:





# ** Consultando as notas de aula, crie um plot de Choropleth do consumo de energia para países usando o dicionário de dados e layout. **

# In[ ]:





# In[ ]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# ##  Choropleth EUA
# 
# ** Importe o arquivo csv 2012_Election_Data usando pandas. **

# In[109]:





# ** Verifique o cabeçalho do DataFrame. **

# In[110]:





# ** Agora crie um gráfico que exiba a idade da população votante (Voting-Age Population, VAP) por estado. Se você quiser mais jogar com outras colunas, certifique-se de considerar seu tipo de dados. O VAP já foi transformado em float para você. **

# In[120]:





# In[121]:





# In[ ]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)

