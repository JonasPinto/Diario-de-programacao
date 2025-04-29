"""
Escreva um programa que leia um número inteiro maior do que 0 e devolva, na tela, a soma de todos os seus algarismos
Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior do que 0, o programa
terminará com a mensagem "Número inválido".
"""
import sys
n = int(input('Digite um número: '))
soma = 0

if n <= 0:
    print('Número inválido')
    sys.exit()
else:
    while n > 0:
        resto = n % 10
        n = n // 10
        soma = soma + resto
        print(resto)
        print(soma)
print(f'A soma dos digitos é {soma}')
