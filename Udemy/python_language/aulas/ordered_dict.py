"""
modulo Collections: Ordered Dict

# Em dicionarios, a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
"""

# Usando ordered dict manten-se a ordem dos elementos
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

# Entendendo a diferença entre Dict e OrderedDict

# Dicionarios comuns

dict1 = {'a': 1, 'b': 2} # A ordem dos elementos não importa
dict2 = {'b': 2,'a': 1}

print(dict1 == dict2) # Para os dicionarios comuns os dois dicionarios são iguais portanto retornara True

# Ordered Dict 
odict1 = OrderedDict({'a': 1, 'b': 2}) # A ordem dos elementos importa
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # Para os dicionarios ORderedDict os dois dicionarios são diferentes portanto retornara False