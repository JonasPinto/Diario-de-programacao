"""
Erros mais comuns em python

É importante prestar atenção e aprender a ler as saídas de erros gerados pela execução do código

Os erros mais comuns:



1 - SyntaxError -> Ocorre quando o python econtra um erro de sintaxe. Ou seja, você escreveu algo que o python não reconhece como parte da linguagem.

Exemplos Syntaxerror

a)
def funcao:
    print('Jonas Pinto')

b)
def = 1

c)
return



2 - NameError -> Ocorre quando uma variável ou função não foi definida.

Exemplos de NameError

a)
print(geek)

b)
geek()



3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

Exemplos TypeError 

a)
print(len(5))

b)
print('jonas' + [])



4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um indice inválido.

Exemplos de IndexError

a)
lista = ['jonas']
print(lista[2])

b)
lista = ['jonas']
print(lista[0][10])



5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas valor inapropriado

Exemplo ValueError

a)
print(int('jonas')) # neste caso nao podemos printar o tipo int com dados string dentro 



6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplos KeyError

a)
dic = {'curso': 'python'}
print(dic['jonas'])


7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.

Exwmplos de AttributeError 

a)
tupla = (11, 2, 31, 4)
print(tuple.sort()) 


8 - IndentationError -> Ocorre quando não respeitamos a indentação do python (4 espaços) ou recuo em um bloco

Exemplos de IdentationError

a)
def nova():
print('jonas')

OBS: Exeptions e Erros são a mesma coisa em python.
OBS: Importante ler e prestar atenção na saída de erro.
"""

