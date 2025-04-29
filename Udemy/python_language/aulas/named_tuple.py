"""
 Módulo Collections - Nmed Tuple

 # Recapitulando tupla
 typla = (1, 2, 3)

 print(tupla[0])
 
 Named Tuple -> São tuplas, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.
 """

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

tor = cachorro(idade=2, raca='sao bernardo', nome='tor')

print(tor)

# Acessando os dados

# Forma 1
print(tor[0]) # idade
print(tor[1]) # raca
print(tor[2]) # nome

# Forma 2
print(tor.idade) # idade
print(tor.raca) # raca
print(tor.nome) # nome

print(tor.index('tor')) # qual o indice do valor 'tor' ?
print(tor.index(2)) # em qual indice esta o valor 2 ?

print(tor.count('sao bernardo')) # quantas vezes 'sao bernardo esta contido na tupla' ?
