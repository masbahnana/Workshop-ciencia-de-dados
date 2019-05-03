#!/usr/bin/env python
# coding: utf-8

# # Curso rápido de Python
# 
# Por favor, note que isso não tem a intenção de ser um curso abrangente de Python ou da programação em geral. Se você não possui experiência de programação, sugiro que dê uma olhada em um outro curso de José Portilla: [Complete Python Bootcamp](https://www.udemy.com/Complete-python-bootcamp/?CouponCode=PY20).
# 
# Este notebook vai apenas passar pelos tópicos básicos em ordem:
# 
# * Tipos de dados
#     * Numbers
#     * Strings
#     * Printando
#     * Listas
#     * Dicionários
#     * Boleanos
#     * Tuplas
#     * Sets
# * Operadores de comparação
# * if,elif, else
# * for Loops
# * while Loops
# * range()
# * list comprehension
# * funções
# * expressões lamda
# * map e filter
# * métodos
# ____

# ## Tipos de dados
# 
# ### Numéricos

# In[1]:


1 + 1


# In[2]:


1 * 3


# In[3]:


1 / 2


# In[4]:


2 ** 4


# In[5]:


4 % 2


# In[6]:


5 % 2


# In[7]:


(2 + 3) * (5 + 5)


# ### Definição de variáveis

# In[8]:


# Não se pode iniciar uma variável com números ou carateres especais
nome_da_variavel = 2


# In[9]:


x = 2
y = 3


# In[10]:


z = x + y


# In[11]:


z


# ### Strings

# In[3]:


'Citação simples'


# In[4]:


"Citações duplas"


# ### Printando

# In[5]:


x = 'ola'


# In[6]:


x


# In[7]:


print(x)


# In[8]:


num = 12
nome = 'Sam'


# In[10]:


print('Meu número é: {one}, e meu nome é: {two}'.format(one=num,two=nome))


# ### Listas

# In[20]:


[1,2,3]


# In[21]:


['hi',1,[1,2]]


# In[12]:


minha_lista = ['a','b','c']


# In[13]:


minha_lista.append('d')


# In[14]:


minha_lista


# In[15]:


minha_lista[0]


# In[16]:


minha_lista[1]


# In[17]:


minha_lista[1:]


# In[18]:


minha_lista[:1]


# In[28]:


minha_lista[0] = 'NOVO'


# In[29]:


minha_lista


# In[30]:


nest = [1,2,3,[4,5,['target']]]


# In[31]:


nest[3]


# In[32]:


nest[3][2]


# In[33]:


nest[3][2][0]


# ### Dicionários

# In[34]:


d = {'chave1':'item1','chave2':'item2'}


# In[35]:


d


# In[36]:


d['chave1']


# ### Booleanos

# In[38]:


True


# In[39]:


False


# ### Tuplas

# In[40]:


t = (1,2,3)


# In[3]:


t[0]


# In[2]:


t[0] = 'NEW'


# ### Sets

# In[43]:


{1,2,3}


# In[44]:


{1,2,3,1,2,1,2,3,3,3,3,2,2,2,1,1,2}


# ## Operadores de comparação

# In[45]:


1 > 2


# In[46]:


1 < 2


# In[47]:


1 >= 1


# In[48]:


1 <= 4


# In[49]:


1 == 1


# In[37]:


'oi' == 'tchau'


# ## Operadores lógicos

# In[51]:


(1 > 2) and (2 < 3)


# In[52]:


(1 > 2) or (2 < 3)


# In[53]:


(1 == 2) or (2 == 3) or (4 == 4)


# ## if,elif, else

# In[38]:


if 1 < 2:
    print('Sim!')


# In[41]:


if 1 < 2:
    print('Primeiro')
else:
    print('Último')


# In[42]:


if 1 > 2:
    print('Primeiro')
else:
    print('Último')


# In[43]:


if 1 == 2:
    print('Primeiro')
elif 3 == 3:
    print('Meio')
else:
    print('Último')


# ## for Loops

# In[45]:


seq = [1,2,3,4,5]


# In[46]:


for item in seq:
    print(item)


# In[47]:


for item in seq:
    print('!')


# In[49]:


for outra_coisa in seq:
    print(outra_coisa+outra_coisa)


# ## while Loops

# In[63]:


i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1


# ## range()

# In[64]:


range(5)


# In[65]:


for i in range(5):
    print(i)


# In[66]:


list(range(5))


# ## list comprehension

# In[67]:


x = [1,2,3,4]


# In[68]:


out = []
for item in x:
    out.append(item**2)
print(out)


# In[69]:


[item**2 for item in x]


# ## Funções

# In[52]:


def my_func(param1='default'):
    """
    Documentação da função vai aqui.
    """
    print(param1)


# In[53]:


my_func


# In[54]:


my_func()


# In[55]:


my_func('novo parametro')


# In[56]:


my_func(param1='novo parametro')


# In[57]:


def square(x):
    return x**2


# In[58]:


out = square(2)


# In[59]:


print(out)


# ## Expressões lamda

# In[62]:


def vezes2(var):
    return var*2


# In[63]:


vezes2(2)


# In[64]:


lambda var: var*2


# ## map e filter

# In[65]:


seq = [1,2,3,4,5]


# In[66]:


map(vezes2,seq)


# In[67]:


list(map(vezes2,seq))


# In[68]:


list(map(lambda var: var*2,seq))


# In[69]:


filter(lambda item: item%2 == 0,seq)


# In[70]:


list(filter(lambda item: item%2 == 0,seq))


# ## Métodos

# In[72]:


st = 'Olá, me chamo Sam'


# In[73]:


st.lower()


# In[74]:


st.upper()


# In[75]:


st.split()


# In[76]:


tweet = 'Dale Grêmio! #Gremio'


# In[77]:


tweet.split('#')


# In[78]:


tweet.split('#')[1]


# In[79]:


d


# In[80]:


d.keys()


# In[81]:


d.items()


# In[82]:


lst = [1,2,3]


# In[83]:


lst.pop()


# In[84]:


lst


# In[85]:


'x' in [1,2,3]


# In[86]:


'x' in ['x','y','z']

