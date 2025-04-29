"""
Listas

listas são mutaveis, ou seja podem ser modificadas ou mudadas.

listas em python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e tambem de podermos colocar QUALQUER tipo de dado.

em c / java: ARREYS
    -Possuem tamanho e tipo de dado fixo:
    OU seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no maximo 5 vaslores.

em python:
    -Dinâmico: Não possui tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adicionando elementos
    -Qualquer tipo de dado: Não possuem tipo de dado fixo; ou seja, podemos colocar qualquer tipo de dado;
as listas em python são representadas por colchetes: []

***********************************************************************************************************************
type([])
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['j', 'o', 'n', 'a', 's', '', 'd', 'a', '', 's', 'i', 'l', 'v', 'a']
lista3 = []
lista4 = list(range(11))
lista5 = list('jonas da silva')

# podemos checar facilmente se determinado valor esta contido na lista

if 8 in lista4:
    print('Encontrei o número 8')
else:
    print('Número não encontrado')

# podemos facilmente ordenar uma lista
lista1.sort()   # lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]  ordenar / organizar uma lista
print(lista1)   # [1, 1, 3, 4, 15, 22, 27, 27, 42, 44, 99]

lista5.sort()   # lista5 = list('jonas da silva')
print(lista5)   # [' ', ' ', 'a', 'a', 'a', 'd', 'i', 'j', 'l', 'n', 'o', 's', 's', 'v']

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))    # count conta o número de vezes que um determinado valor se encontra em uma lista
print(lista5.count('e'))

***********************************************************************************************************************
# adicionar elementos em listas
Para adicionar elementos em listas, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# OBS: com append conseguimos adicionar um elemento por vez
# lista.append(12, 34, 56)  # Erro

lista1.append([8, 3, 1])  # Aceita valor único,  coloca a lista como elemento único
print(lista1)

lista1.extend([123, 44, 67])  # Aceita diversos valores, coloca cada elemento passado individualmente
print(lista1)

# podemos inserir um novo elemento na lista informando a posição do indice
lista1.insert(2, 'novo valor') # insert apenas coloca o valor na posição passada
print(lista1)

***********************************************************************************************************************
# podemos facilmente juntar 2 listas
lista1 = lista1 + lista2  # junta s lista2 com a lista1
lista1.extend(lista2)     # junta a lista2 com a lista1
print(lista1)

***********************************************************************************************************************
# podemos inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

***********************************************************************************************************************
# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

***********************************************************************************************************************
# Podemos contar quantos elementos existem na lista
print(len(lista5))

***********************************************************************************************************************
# Podemos remover o ultimo elemento de uma lista
# OBS: O pop não somente remove o ultimo elemento mas tambem o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos á direita deste indice serão deslocados par a esquerda.

lista5.pop(2)  # Remove o elemento na posição 2
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

***********************************************************************************************************************
# Podemos repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

***********************************************************************************************************************
# Podemos converter uma string para uma lista

# Exemplo 1
curso = 'programação em python'
print(curso)
curso = curso.split()  # split separa os elementos pelos espaços entre eles
print(curso)

# Exemplo 2
curso = 'progaramação,em,python'
print(curso)
curso = curso.split(',')  # pode-se indicar o parametro de separação
print(curso)

***********************************************************************************************************************
# Convertendo uma lista em uma string

lista6 = ['programação', 'em', 'Python']
print(lista6)

# pega a lista e coloca espaço entre cada elemento e transforma em string
curso = ' '.join(lista6)  # Dentro do espaço pode ser inserido qualquer divisor. Exemplo '%'.join(lista6)
print(curso)

***********************************************************************************************************************
# Pode-se colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, 'jonas', 'a', [1, 2, 3], 452478745]
print(lista6)
print(type(lista6))

***********************************************************************************************************************
# Iterando sobre listas

# Exemplo 1 - Utilizando for
soma = 0
for elemento in lista1:

    print(elemento, end=' ')
    soma = soma + elemento
print('\n', soma)


# Exemplo 2 - Utilizando while
carrinho = []  # lista vazia podemos adicionar itens dentro dela
produto = ''   #
while produto != 'sair':
    print("Adicione um produto na lista\n"
          "ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto, end=' ')

***********************************************************************************************************************
# Utilizando variaveis em listas
numero = [1, 2, 4, 5, ]

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

***********************************************************************************************************************
# Fazemos acesso aos elementos de forma idexada
#           0         1         2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Fazer acesso aos elementos de forma indexada inversa
# pensar na lista como um circulo onde o final de um elemento esta ligado ao inicio da lista
print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # azul
print(cores[-5])  # Erro, pois não existe indice -5

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

cores = ['verde', 'amarelo', 'azul', 'branco']
# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

***********************************************************************************************************************
# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)

***********************************************************************************************************************
# outros metodos não tão importantes mas também úteis

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice da lista está o valor 6?
print(numeros.index(6))  # Se houver numeros repetidos traz o primeiro valor encontrado na lista

# Em qual índice da lista está o valor 9?
print(numeros.index(9))

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))  # Encontre o próximo valor 5 a partir do indice 1
print(numeros.index(5, 2, 6))  # Encontre o proximo valor 5 entre o indice 2 e 6
print(numeros.index(5, 3))  # Encontre o proximo valor 5 a partir do indice 3

# print(numeros.index(5, 4))  # Encontre o proximo valor 5 a partir do indice 4
# OBS: Caso não tenha este elemento na lista, será apresentado -> ValueError


***********************************************************************************************************************
# Revisão de slicing
# lista [::]  -> [inicio:fim:passo]
# range [::]  -> [      :   :     ]

# Trabalhando com slice de lista
lista =[1, 2, 3, 4]
# Inicio
print(lista[1:])  # inicio no indice 1 e pega todos os outros restantes
# Fim
print(lista[:2])  # começa no indice 0 e vai até o indice 2 -1
print(lista[:4])  # começa no indice 0 e vai até o indice 4 -1
print(lista[0:3]) # começa no indice 0 e vai até o indice 3 - 1
# Passo
print(lista[1::2])  # Começa em 1 vai até o final de 2 em 2
print(lista[::2])   # Começa em 0 vai até o final de 2 em 2
print(lista[::-1])  # Começa em 0 vai até o final com passo -1

***********************************************************************************************************************
# invertendo valores em uma lista
nome = ['jonas', 'silva']
print(nome)  # ['jonas', 'silva']
nome[0], nome[1] = nome[1], nome[0]
print(nome)  # ['silva', 'jonas']

nome.reverse()  # inverte a lista
print(nome)

# Soma*, Valor Maximo*, Valor Minimo*, Tamanho
# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma toda a lista
print(max(lista))  # máximo valor da lista
print(min(lista))  # mínimo valor da lista
print(len(lista))  # tamanho da lista

***********************************************************************************************************************
# Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))
[1, 2, 3, 4, 5, 6]
<class 'list'>

lista = tuple(lista)
print(lista)
print(type(lista))
(1, 2, 3, 4, 5, 6)
<class 'tuple'>

***********************************************************************************************************************
# Desempacotamento de listas
lista = [1, 2, 3]
num1, num2, num3 = lista  # lista atribui os valores da lista cada um a uma variavel
print(num1)
print(num2)
print(num3)

***********************************************************************************************************************
# Copiando uma lista para outra (Shellow Copy e Deep Copy)


# forma 1 - deep copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)
# Ao utilizarmos lista.copy() copiamos os dados da lista para uma outra lista, mas elas ficaram
# totalmente endependentes, ou seja, modificando uma lista não afeta a outra. isso em python é chamado de deep copy


# Forma 2 - shallow copy
lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)

nova.append(4)
print(lista)
print(nova)
# A copia via atribuição modifica a lista atual e a anterior. isso em python é cahmado de shellow copy
"""
def ValorLista():
    for i in range(1,5):
        lista.append(int(input(f'Digite o Valor da sua prova {i}: ')))

def Media():
    lista.sort()
    s = 0

    for i in range(len(lista)):
        lista[i]
        s = s + lista[i]   
    m = s/4
    return m


lista = []
ValorLista()
print(lista)

nota_media = Media()
print(nota_media)