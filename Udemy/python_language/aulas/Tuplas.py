"""
Tuplas (tuple)
Tuplas são bastante parecidas com listas
Exixtem duas diferenças basicas
1 - Tuplas são representadas por parênteses () e tambem a virgula
2 - Tuplas são imutáveis isso significa que ao se criar uma tupla ela não muda
toda operação em uma tupla gera uma nova tupla.


# cuidado 1: As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6

print(tupla2)
print(type(tupla2))

# cuidado 2: Tuplas com 1 elemento

tupla3 = (4)   # isso não é uma tupla para ser tupla deveria ser = (4,)
print(tupla3)
print(type(tupla3))
# tuplas são definidas pela virgula não pelos parenteses
(4) -> Não é tupla
(4,) -> É tupla
4, -> É Tupla

# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla
tupla = ('jonas', 'pinto')
firstname, lastname = tupla

print(lastname)
print(firstname)
print(tupla)

Métodos para adição e remoção de elementos nãp podem ser aplicados as tuplas pois são imutavei
pode-se utilizar sum, max, min, len  se os valores forem inteiros ou reais, com ecessão de len que pode contar quantos
elementos possuem na tupla.

tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))


tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print(tupla1 + tupla2) # -> (1, 2, 3, 4, 5, 6)
print(tupla1) # -> (1, 2, 3)
print(tupla2) # -> (4, 5, 6)

# tuplas são imutaveis, mas podemos sobrescrever seus valores
tupla1 = tupla1 + tupla2
print(tupla1)

# verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)  # -> True

tupla = (1, 2, 3)

for n in tupla:
    print(n, end=' ')

for indice, valor in enumerate(tupla):
    print('\n', indice, valor)

# contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('b'))

nome = tuple('Jonas da siva pinto'.lower())
print(nome)
print(nome.count(''))

# Dicas na utilização de tuplas
# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção
# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abriu', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembtro', 'Dezembro')
# O a elementos de uma tupla também é semelhante a de uma lista
print(meses[0:3])

# iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

"""
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abriu', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembtro', 'Dezembro')

# Verificamos em qual índice um elemento está na tupla
print(meses.index('Maio'))  # tomar cuidado com letras maiusculas e minusculas

# Por que utilizar tuplaas ?
# - Tuplas são mais rapidas do que listas
# - Tuplas deixam seu codigo mais seguro -> são imutaveis e isso traz mais segurança ao codigo

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # na tupla nao temos o problema de shellow copy

print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra
print(nova)
print(outra)



