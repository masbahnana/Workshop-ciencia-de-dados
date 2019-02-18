# Workshop-ciencia-de-dados
Workshop de Ciência de Dados de iniciantes a intermediário 

## Jupyter notebook pela internet 
Caso tu não queira ou não tenha espaço disponível no teu computador para o pacote Anaconda, também conseguimos utilizar ele na versão web.
[Jupyter](https://jupyter.org/try)
Depois é só clicar em "Try Jupyter with Python" e pronto! 

Obs: optando por utilizar o Jupyter notebook via browser, tu não precisas instalar as bibliotecas.

## Instalando o Anaconda

### No Linux
Download Anaconda Python version 3,6 no site [Anaconda](https://www.anaconda.com/distribution/)
Rode o Download na linha de comando conforme abaixo:

    "cd ~/Downloads/"

    "./Anaconda3-5.0.1-Linux-x86_64.sh"
    
    "bash Anaconda3-5.0.1-Linux-x86_64.sh"

Você será solicitado a dizer sim. Depois deve seguir todas as instruções onde o Python anaconda será instalado.
Abra um novo terminal e verifique os pontos padrão do python para 3.6.4 digitando:

    "python3"

Obs: caso tu estejas instalando outra versão do python, será necessário alterá-la no comando de instalação.

### No Windows

Faça o Download Anaconda Python version 3,6 no site [Anaconda](https://www.anaconda.com/distribution/)
Após é só seguir a instalação como qualquer software no windows 

## Instalando as bibliotecas utilizadas nesse workshop: 
Via pip:

    "python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose"
    "python -m pip install numpy scipy matplotlib"

Via conda: 

    "conda install -c anaconda numpy" 

Via Linux package manager:

    "sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose"
    "sudo dnf install numpy scipy python-matplotlib ipython python-pandas sympy python-nose atlas-devel"


