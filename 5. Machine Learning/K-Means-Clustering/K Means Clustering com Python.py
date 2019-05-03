#!/usr/bin/env python
# coding: utf-8

# # K Means Clustering com Python
# 
# Este notebook é apenas um código de referência para o acompanhamento do vídeo e da leitura
# 
# ## Método usado
# 
# K Means Clustering é um algoritmo de aprendizagem sem supervisão que tenta agrupar dados com base em sua similaridade. A aprendizagem não supervisionada significa que não há resultados a serem previstos, e o algoritmo apenas tenta encontrar padrões nos dados. No K means clustering temos a especificar o número de clusters nos quais os dados devem ser agrupados. O algoritmo atribui aleatoriamente cada observação a um cluster e encontra o centróide de cada cluster. Então, o algoritmo itera através de duas etapas:
# Reatribui pontos ao cluster cujo centroide é o mais próximo e calcula o novo centróide de cada cluster. Estes dois passos são repetidos até que a variação dentro do cluster não possa ser mais reduzida. A variação dentro do cluster é calculada como a soma da distância euclidiana entre os pontos de dados e seus respectivos centroides do cluster.

# ## Importa bibliotecas

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Cria dados

# In[2]:


from sklearn.datasets import make_blobs


# In[3]:


data = make_blobs(n_samples=200, n_features=2, 
                           centers=4, cluster_std=1.8,random_state=101)


# ## Visualizando os dados data

# In[4]:


plt.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')


# ## Criando os clusters

# In[5]:


from sklearn.cluster import KMeans


# In[6]:


kmeans = KMeans(n_clusters=4)


# In[7]:


kmeans.fit(data[0])


# In[8]:


kmeans.cluster_centers_


# In[9]:


kmeans.labels_


# In[10]:


f, (ax1, ax2) = plt.subplots(1, 2, sharey=True,figsize=(10,6))
ax1.set_title('K Means')
ax1.scatter(data[0][:,0],data[0][:,1],c=kmeans.labels_,cmap='rainbow')
ax2.set_title("Original")
ax2.scatter(data[0][:,0],data[0][:,1],c=data[1],cmap='rainbow')


# Você deve notar que as cores não têm relação entre as duas parcelas
