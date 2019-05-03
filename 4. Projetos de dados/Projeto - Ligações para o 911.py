#!/usr/bin/env python
# coding: utf-8

# # Projeto: Ligações para o 911

# Para este projeto estaremos analisando alguns dados de chamadas para o 911 do [Kaggle](https://www.kaggle.com/mchirico/montcoalert). Os dados contém os seguintes campos:
# 
# * lat: Variável String, Latitude
# * lng: Variável String, Longitude
# * desc: Variável String, Descrição da Chamada de Emergência
# * zip: Variável String, CEP
# * título: Variável String, Título
# * timeStamp: Variável String, AAAA-MM-DD HH: MM: SS
# * twp: Variável String, Township
# * addr: Variável String, Endereço
# * e: Variável String, variável Dummy (sempre 1)
# 
# Simplesmente acompanhe este notebook e tente completar as instruções ou responder as perguntas em negrito usando suas habilidades Python e Data Science!

# ## Dados e Configuração

# ** Importar numpy e pandas **

# In[129]:





# ** Importe as bibliotecas de visualização e configure% matplotlib inline. **

# In[130]:





# ** Leia o arquivo csv como um dataframe chamado df **

# In[131]:





# ** Verifique a info() do df **

# In[132]:





# ** Verifique o cabeçalho do df **

# In[155]:





# ## Perguntas básicas

# ** Quais são os top 5 CEPs nas chamadas 911? **

# In[134]:





# ** Quais são os 5 principais municípios nas chamadas 911? **

# In[135]:





# ** Dê uma olhada na coluna 'title'. Quantos códigos de título exclusivos existem? **

# In[136]:





# ## Criando novos recursos

# ** Na coluna "title" existem "Razões / Departamentos" especificados antes do código do título. Estes são "EMS", "Fire" e "Traffic". Use .apply () com uma expressão lambda personalizada para criar uma nova coluna chamada "Razão" que contém esse valor de string. **
# 
# ** Por exemplo, se o valor da coluna do título for EMS: BACK PAINS / BLESSOR, o valor da coluna Reason seria EMS. **

# In[137]:





# ** Qual é o motivo mais comum para uma chamada do 911 com base nessa nova coluna? **

# In[138]:





# ** Agora use Seaborn para criar um countplot de chamadas 911 baseadas nesta nova coluna. **

# In[139]:





# ** Agora vamos começar a focar em informações de tempo. Qual é o tipo de dados dos objetos na coluna timeStamp? **

# In[140]:





# ** Você deveria ter notado que esses timestamps ainda são strings. Use [pd.to_datetime](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html) para converter a coluna de strings em objetos DateTime. **

# In[184]:





# ** Agora você pode pegar atributos específicos de um objeto Datetime chamando-os. Por exemplo:**
# 
#     time = df['timeStamp'].iloc[0]
#     time.hour
# 
# ** Você pode usar o método de consulta de funções do Jupyter (Tab) para explorar os vários atributos que você pode chamar. Agora que a coluna timestamp é realmente objetos DateTime, use .apply () para criar 3 novas colunas chamadas Hour, Month e Day of Week. Você criará essas colunas com base na coluna timeStamp, consulte as soluções se você ficar preso nesta etapa. **

# In[142]:





# ** Observe como o dia da demana é um número inteiro de 0-6. Use o .map () com este dicionário para mapear os nomes das seqüências reais para o dia da semana: **
# 
#     dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

# In[143]:





# In[144]:





# ** Agora use Seaborn para criar um countplot da coluna "Day of Week" com a tonalidade baseada na coluna Reason. **

# In[168]:





# ** Agora faça o mesmo para o mês: **

# In[3]:





# ** Você notou algo estranho no Plot? **
# 
# _____
# 
# ** Você deve ter notado que estavam faltando alguns meses. Vejamos se podemos talvez preencher essa informação ao traçar as informações de outra forma, possivelmente um plot de linha simples que preencha os meses que faltam. Para fazer isso, precisamos trabalhar com pandas...

# ** Agora, crie um objeto groupby chamado "byMonth", onde você agrupa o DataFrame pela coluna do mês e use o método count() para agregação. Use o método head() neste DataFrame retornado. **

# In[169]:





# ** Agora crie um plot simples fora do Dataframe indicando a contagem de chamadas por mês. **

# In[175]:





# ** Agora veja se você pode usar o lmplot () do Seaborn para criar um modelo linear no número de chamadas por mês. Tenha em mente que talvez seja necessário resetar o índice em uma coluna. **

# In[187]:





# ** Crie uma nova coluna chamada 'Data' que contenha a data da coluna timeStamp. Você precisará usar .apply() junto com o método .date(). **

# In[193]:





# ** Agora agrupe esta coluna Data com o groupby. Usando o count (), crie um gráfico de contagens de chamadas 911. **

# In[197]:





# ** Agora recrie esse plot, mas crie 3 plots separados com cada plot representando uma Razão para a chamada 911 **

# In[199]:





# In[201]:





# In[202]:





# ____
# ** Agora vamos continuar a criar mapas de calor com seaborn e nossos dados. Em primeiro lugar, devemos reestruturar o quadro de dados para que as colunas se tornem horas e o Índice se torne o Dia da Semana. Há muitas maneiras de fazer isso, mas eu recomendaria tentar combinar groupby com o método [unstack](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.unstack.html) . Consulte as soluções se você ficar preso nisso! **

# In[203]:





# ** Agora crie um mapa de calor usando este DataFrame **

# In[204]:





# ** Agora crie um clustermap usando este DataFrame. **

# In[205]:





# ** Agora repita estes mesmos plots e operações para um DataFrame que mostra o mês como a coluna. **

# In[207]:





# In[208]:





# In[209]:




