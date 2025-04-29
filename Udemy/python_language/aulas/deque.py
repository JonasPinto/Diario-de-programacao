"""
módulo collections - Deque 
Podemos dizer que o deque é uma lista de alta performance, praticamente igual a lista mas podendo se adicionar e remover elementos a esquerda.
"""
from collections import deque

list = deque('jonas')
print(list) # deque(['j', 'o', 'n', 'a', 's'])

list.appendleft('s') # adiciona um elemento a esquerda, se usado apenas append adiciona a direita(na ultima posição)

print(list) # deque(['s', 'j', 'o', 'n', 'a', 's'])
list.popleft() # remove o primeiro elemento da esquerda, se usado apenas pop remove o ultimo elemento

print(list) # deque(['j', 'o', 'n', 'a', 's'])