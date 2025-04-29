"""
https://docs.python.org/3/library/collections.html?highlight=collections#collections.defaultdict

Modulo Collections - Defalt Dict

# Recap Dicionaros

Dicionario = {'curso': 'programação em python: Essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) # KeyError

Defalt Dict -> Ao criar um dicionarioutilizando-o, nós informamos um valor defalt, podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver um valor definido, Caso tentemos acessar uma chave que não existe, essa chave será criada e o valor defalt será atribuido.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores. 
"""
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'programação em python: Essencial'

print(dicionario)

print(dicionario['outro']) # No dicionario comun teriamos um Key error, mas aqui não

print(dicionario)
