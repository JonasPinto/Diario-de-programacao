"""
12. Ler um número inteiro. Se o número lido for negativo, escreva a mensagen "Número inválido". Se o número for positivo
caucular o logaritimo deste número.
"""
import math
num = int(input('Digite um número inteiro: '))
base = int(input('Digite a base desejada: '))

if num < 0:
    print('Número invalido')
else:
    log = math.log(num, base)
    print(f'O logaritimo de {num} é {log} ')




