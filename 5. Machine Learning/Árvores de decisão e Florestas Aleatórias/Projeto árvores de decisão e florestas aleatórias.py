#!/usr/bin/env python
# coding: utf-8

# # Projeto florestas aleatórias
# 
# Para este projeto, estaremos explorando dados disponíveis publicamente de [LendingClub.com](www.lendingclub.com). Lending Club conecta pessoas que precisam de dinheiro (mutuários) com pessoas que têm dinheiro (investidores). Felizmente, como investidor, você gostaria de investir em pessoas que mostraram um perfil de ter uma alta probabilidade de pagá-lo de volta. Vamos tentar criar um modelo que ajude a prever isso.
# 
# O clube de empréstimo teve um [ano muito interessante em 2016](https://en.wikipedia.org/wiki/Lending_Club#2016), então vamos verificar alguns de seus dados e ter em mente o contexto. Esses dados são de antes mesmo de serem públicos.
# 
# Utilizaremos os dados de empréstimos de 2007-2010 e tentaremos classificar e prever se o mutuário pagou o empréstimo na íntegra. Você pode baixar os dados de [aqui](https://www.lendingclub.com/info/download-data.action) ou apenas usar o csv já fornecido. Recomenda-se que você use o csv fornecido, uma vez que foi limpo dos valores de NA.
# 
# Aqui estão o que as colunas representam:
# * credit.policy: 1 se o cliente atender aos critérios de subscrição de crédito da LendingClub.com e 0 caso contrário.
# * purpose: O objetivo do empréstimo (leva valores "credit_card", "debt_consolidation", "educacional", "grande compra", "small_business" e "all_other").
# * int.rate: a taxa de juros do empréstimo (uma taxa de 11% seria armazenada como 0,11). Os mutuários julgados por LendingClub.com para serem mais arriscados recebem taxas de juros mais elevadas.
# * installment: as parcelas mensais devidas pelo mutuário se o empréstimo for financiado.
# * log.annual.inc: O log natural da renda anual auto-relatada do mutuário.
# * dti: Ratio dívida / rendimento do tomador do empréstimo (montante da dívida dividido pela receita anual).
# * fico: a pontuação de crédito FICO do mutuário.
# * days.with.cr.line: O número de dias em que o mutuário teve uma linha de crédito.
# * revol.bal: Saldo rotativo do mutuário (montante não pago no final do ciclo de cobrança do cartão de crédito).
# * revol.util: taxa de utilização da linha rotativa do mutuário (o valor da linha de crédito usada em relação ao crédito total disponível).
# * inq.last.6mths: número de consultas do mutuário por credores nos últimos 6 meses.
# * delinq.2yrs: o número de vezes que o mutuário havia passado mais de 30 dias em um pagamento nos últimos 2 anos.
# * pub.rec: O número de registros públicos depreciativos do mutuário (arquivamentos de falências, ônus fiscais ou julgamentos).

# # Importar bibliotecas
# 
# ** Importe as bibliotecas usuais para pandas e plotagem. Você pode importar sklearn mais tarde. **

# In[2]:





# ## Obter dados
# 
# ** Use pandas para ler loan_data.csv como um DataFrame chamado loans. **

# In[3]:





# ** Use os métodos info(), head(), e describe() em loans. **

# In[4]:





# In[5]:





# In[6]:





# # Análise exploratória de dados 
# 
# Vamos fazer alguma visualização de dados! Usaremos os recursos de plotagem incorporados ao seaborn e ao pandas, mas sinta-se livre para usar qualquer biblioteca que você deseja. Não se preocupe com as cores, apenas se preocupe em obter a idéia principal do plot.
# 
# ** Crie um histograma de duas distribuições FICO umas sobre as outras, uma para cada um dos valores possíveis de credit.policy **.
# 
# * Nota: Isto é bastante complicado, sinta-se à vontade para fazer referência às soluções. Você provavelmente precisará de uma linha de código para cada histograma, eu também recomendo usar o .hist() incorporado ao pandas. *

# In[7]:





# ** Crie uma figura semelhante, mas dessa vez use a coluna not.fully.paid. **

# In[8]:





# ** Crie um countplot usando seaborn mostrando a contagens de empréstimos por finalidade, com a matiz de cor definido por not.fully.paid. **

# In[9]:





# ** Veja a tendência entre o índice FICO e a taxa de juros. Recrie o seguinte jointplot. **

# In[10]:





# ** Crie os seguintes lmplots para ver se a tendência diferiu entre not.fully.paid e credit.policy. Verifique a documentação para lmplot() se você não consegue descobrir como separá-lo em colunas. **

# In[11]:





# # Configurando os dados
# 
# Vamos nos preparar para configurar nossos dados para o nosso modelo de classificação de florestas aleatórias!
# 
# ** Verifique loans.info() novamente. **

# In[12]:





# ## Recursos categóricos
# 
# Observe a coluna ** purpose ** como categórica.
# 
# Isso significa que precisamos transformá-los usando variáveis dummys para que Sklearn possa compreendê-las. Vamos fazer isso em um passo limpo usando pd.get_dummies.
# 
# Vamos mostrar uma maneira de lidar com essas colunas que podem ser expandidas para múltiplos parâmetros categóricos, se necessário.
# 
# ** Crie uma lista de 1 elemento contendo a string 'purpose'. Chame esta lista de cat_feats. **

# In[13]:





# ** Agora use "pd.get_dummies(loans, columns = cat_feats, drop_first = True)" para criar um DataFrame maior fixo que tenha novas colunas de recursos com variáveis dummy. Chame este dataframe de final_data. **

# In[14]:





# In[ ]:





# ## Divisão Treino-Teste de dados
# 
# Agora é hora de dividir nossos dados em um conjunto de treinamento e um conjunto de testes!
# 
# ** Use sklearn para dividir seus dados em um conjunto de treinamento e um conjunto de testes como fizemos no passado. **

# In[16]:





# In[17]:





# ## Training a Decision Tree Model
# 
# Vamos começar treinando uma única árvore de decisão primeiro!
# 
# ** Import DecisionTreeClassifier **

# In[18]:


from sklearn.tree import DecisionTreeClassifier


# ** Crie uma instância de DecisionTreeClassifier() chamada dtree e fite-a com os dados de treinamento. **

# In[19]:





# In[32]:





# ## Previsões e avaliação da árvore de decisão
# ** Faça previsões do conjunto de teste e crie um relatório de classificação e uma matriz de confusão. **

# In[21]:





# In[22]:





# In[23]:





# In[24]:





# ## Treinando o modelo de florestas aleatórias
# 
# Agora é hora de treinar nosso modelo!
# 
# ** Crie uma instância da classe RandomForestClassifier e ajuste-a aos nossos dados de treinamento da etapa anterior. **

# In[25]:





# In[26]:





# In[27]:





# ## Previsões e Avaliação
# 
# Vamos prever os valores do y_test e avaliar o nosso modelo.
# 
# ** Preveja a classe de not.fully.paid para os dados X_test. **

# In[28]:





# ** Agora crie um relatório de classificação dos resultados. Você recebe algo estranho ou algum tipo de aviso? **

# In[29]:





# In[30]:





# ** Mostre a Matriz de Confusão para as previsões. **

# In[31]:





# ** O que performou melhor: a floresta aleatória ou a árvore de decisão? **

# In[36]:




