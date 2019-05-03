#!/usr/bin/env python
# coding: utf-8

# # Exercício de visualização de dados Pandas
# 
# Este é apenas um exercício rápido para você rever os vários gráficos que mostramos anteriormente. Use ** df3 ** para replicar os seguintes gráficos.

# In[14]:


import pandas as pd
import matplotlib.pyplot as plt
df3 = pd.read_csv('df3')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


df3.info()


# In[16]:


df3.head()


# ** Recrie este gráfico de dispersão de b vs a. Observe a cor e o tamanho dos pontos. Observe também o tamanho da figura. Veja se você consegue descobrir como alongá-lo de forma semelhante. Se precisar, volte algumas seções ... **

# In[4]:





# ** Crie um histograma da coluna 'a'. **

# In[5]:





# ** Estes plots estão ok, mas elas não parecem muito profissionais. Use folhas de estilo para definir o estilo em 'ggplot' e refazer o histograma de cima. Veja também como adicionar mais barras.

# In[6]:





# In[7]:





# ** Crie um boxplot comparando as colunas a e b. **

# In[8]:





# ** Criar um plot "kde" da coluna 'd' **

# In[9]:





# ** Descubra como aumentar a largura de linha e fazer o linestyle pontilhado. **

# In[10]:





# ** Crie um gráfico de área de todas as colunas para apenas as linhas até 30. (sugestão: use .ix). **

# In[15]:





# ## Desafio bonus!
# Note, você pode achar isso realmente difícil, volte às soluções se você não conseguir descobrir.
# ** Observe como a legenda em nossa figura anterior sobrepôs alguns dos diagramas reais. Você pode descobrir como exibir a legenda fora do plot, conforme mostrado abaixo? **
# 
# ** Tente pesquisar o Google para obter um bom link no stackoverflow sobre este tópico. Se você não consegue encontrá-lo sozinho - [aqui vai uma dica.](Http://stackoverflow.com/questions/23556153/how-to-put-legend-outside-the-plot-with-pandas ) **

# In[17]:




