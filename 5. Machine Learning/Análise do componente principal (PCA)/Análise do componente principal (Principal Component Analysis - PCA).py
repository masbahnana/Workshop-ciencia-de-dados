#!/usr/bin/env python
# coding: utf-8

# # Análise do componente principal (Principal Component Analysis - PCA)
# 
# Vamos discutir PCA! Uma vez que este não é exatamente um algoritmo de Machine Learning completo, mas apenas um algoritmo de aprendizagem não supervisionado, teremos apenas uma palestra sobre este assunto, mas nenhum projeto completo de Machine Learning (embora possamos trabalhar no conjunto de câncer com PCA).
# 
# ## Revisão de PCA
# 
# Certifique-se de assistir ao de vídeo de apresentação teórica para uma visão geral completa da PCA!
# Lembre-se de que o PCA é apenas uma transformação dos seus dados e tenta descobrir quais recursos explicam a maior variação em seus dados. Por exemplo:

# <img src='PCA.png' />

# ## Bibliotecas

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Os dados
# Vamos trabalhar com o conjunto de dados de câncer novamente, pois ele tem muitos atributos.

# In[2]:


from sklearn.datasets import load_breast_cancer


# In[3]:


cancer = load_breast_cancer()


# In[4]:


cancer.keys()


# In[5]:


print(cancer['DESCR'])


# In[6]:


df = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])


# In[7]:


df.head()


# ## Visualização de PCA
# 
# Como observamos antes, é difícil visualizar dados com muitas dimensões. Podemos usar o PCA para encontrar os dois primeiros componentes principais e visualizar os dados neste novo espaço bidimensional, com um único espaço de dispersão. Antes de fazer isso, precisamos escalar nossos dados para que cada parâmetro tenha uma variância unitária.

# In[8]:


from sklearn.preprocessing import StandardScaler


# In[9]:


scaler = StandardScaler()
scaler.fit(df)


# In[10]:


scaled_data = scaler.transform(df)


# O PCA com o Scikit Learn usa um processo muito semelhante a outras funções de pré-processamento que acompanham o SciKit Learn. Nós instanciamos um objeto PCA, localizamos os componentes principais usando o método de ajuste e, em seguida, aplicamos a rotação e a redução da dimensionalidade chamando transform().
# 
# Também podemos especificar quantos componentes queremos manter ao criar o objeto PCA.

# In[11]:


from sklearn.decomposition import PCA


# In[12]:


pca = PCA(n_components=2)


# In[13]:


pca.fit(scaled_data)


# Agora, podemos transformar esses dados em seus dois primeiros componentes principais.

# In[14]:


x_pca = pca.transform(scaled_data)


# In[15]:


scaled_data.shape


# In[16]:


x_pca.shape


# Ótimo! Reduzimos 30 dimensões para apenas 2! Vamos oplotar essas duas dimensões.

# In[17]:


plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'],cmap='plasma')
plt.xlabel('First principal component')
plt.ylabel('Second Principal Component')


# Claramente, usando esses dois componentes, podemos separar facilmente essas duas classes.
# 
# ## Interpretando os componentes
# 
# Infelizmente, com este grande poder de redução da dimensionalidade, vem o custo de poder entender o que esses componentes representam.
# 
# Os componentes correspondem a combinações dos recursos originais. Os próprios componentes são armazenados como um atributo do objeto PCA ajustado:

# In[55]:


pca.components_


# Nessa matriz numérica, cada linha representa um componente principal e cada coluna se relaciona com os recursos originais. podemos visualizar esta relação com um mapa de calor:

# In[18]:


df_comp = pd.DataFrame(pca.components_,columns=cancer['feature_names'])


# In[20]:


plt.figure(figsize=(12,6))
sns.heatmap(df_comp,cmap='plasma',)

