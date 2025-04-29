""" Conjuntos 
- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à teoria dos comjuntos da matematica
- Aqui no python, os conjuntos são chamados de sets
dito isto, da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles
Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em python com chaves {} 

Diferença entre Conjuntos (set) e Mapas (dicionarios) em python:
   - Um dicionario tem chave/valor;
   - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos
print(s)
print(type(s))
# OBS: Ao criar um conjunto com valores repetidos os conjuntos eliminam as repetições

# Forma 2
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento esta contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# importante lembrar que, além de não termos valores duplicados, não temos ordem
dados = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34

# listas aceitam valores duplicados, então teremos 10 elementos
lista = list(dados)
print(f'Lista: {lista} com {len(lista)} elementos')

# tuplas aceitam valores duplicados, então teremos 10 elementos 
tupla = tuple(dados)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios não aceitam chave duplicada por isso teremos 8 elementos
dicionario = {}.fromkeys(dados, 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados por isso teremos 8 elementos 
conjunto = set(dados)
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados, em sets(conjuntos) tambem podemos

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets 
# Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu e os visitantes informam manualmente a cidade de onde vieram

# Nós adicionamos cada cidade em uma lista python, já que em lista nós podemos adicionar novos elementos e ter repetições 


cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos

# Podemos utilizar o set para isso:
print(len(set(cidades)))
cidades_sem_repeticoes = set(cidades) # set tira as repetições
print(cidades_sem_repeticoes) # -> {'Cuiaba', 'Belo Horizonte', 'São Paulo', 'Campo Grande'}

# Adicionando elemento em um conjunto
s = {1, 2, 3}
s.add(4)
s.add(4) # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado
print(s)

# Remover elementos em um conjunto

# Forma 1
s = {1, 2, 3}
s.remove(3) # Não é indice é o valor a ser removido
            # caso o valor não seja encontrado será gerado um erro keyerror
print(s)

# Forma 2
s.discard(4) # Ao usar o discard passando um avalor não existente não é retornado erro como no remove
print(s)

s = {1, 2, 3}
# Copiando um cojunto para outro

# Forma 1 - Deep Copy
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shellow Copy

novo = s 

novo.add(4)

print(novo)
print(s)

s.clear()
print(s)

estudantes_python = {'marcos', 'patricia', 'ellen', 'pedro', 'julia', 'guilherme'}
estudantes_java = {'fernando', 'gustavo', 'julia', 'ana', 'patricia'}

# veja que alguns alunos que estudam python tambem estudam java
# precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe -> |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos
# Forma 1 Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizand o & 
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Metodos matematicos de conjuntos
#imagine que temos dois conjuntos: Um contendo estudantes do curso de python e um contendo estudantes do curso de java

# Gerar um conjunto de estudantes que não estão no outro
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# soma*, Valor Maximo*, Valor Minimo*, Tamanho
# Se os valores forem todos inteiros ou reais
s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

# dir(s)

# ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""
# soma*, Valor Maximo*, Valor Minimo*, Tamanho
# Se os valores forem todos inteiros ou reais
s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))