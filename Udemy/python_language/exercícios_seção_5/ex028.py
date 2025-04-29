"""
Faça um programa que leia trez números positivos inteiros e efetue o cauculo de uma das seguintes médias de acordo com um valor númerico
digitado pelo usuário:
A geometrica
B ponderada
C harmônica
D aritimética
"""

from sys import exit

print('      \033[31mCALCULADORA DE MÉDIA\033[m      ')
print('ESCOLHA UMA DAS OPÇÕES')
print('\033[35m[A] GEOMÉTRICA\033[m\n\033[32m[B] PONDERADA\033[m\n\033[33m[C] HARMÔNICA\033[m\n\033[34m[D] ARITIMÉTICA\033[m')
op = input().lower()
if (op != 'a') and (op != 'b') and (op != 'c') and (op != 'd'):
    print('OPÇÃO INVALIDA')
    exit()
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = int(input('Digite o terceiro número: '))

if op == 'a':
    re = x * y * z
    re = re ** 0.333333333333
    print(f'A média geométrica dos números digitados é \033[34m{re:.2f}\033[m')
elif op == 'b':
    re = (x + (2 * y) + (3 * z)) / 6
    print(f'A média ponderada dos números digitados é \033[34m{re}\033[m')
elif op == 'c':
    re = 1 / ((1 / x) + (1 / y) + (1 / z))
    print(f'A média harmônica dos números digitados é \033[34m{re:.3f}\033[m')
elif op == 'd':
    re = (x + y + z) / 3
    print(f'A média aritimética dos números digitados é \033[34m{re}\033[m')

