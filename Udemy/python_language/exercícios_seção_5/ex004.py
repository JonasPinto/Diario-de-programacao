# Faça um programa que leia um número e, caso ele seja positivo, caucule e mostre:
# - O número digitado
# - A raiquadrada do número digitado
num = float(input('Digite um número: '))
if num > 0:
    print(f'O número digitado foi {num}')
    raiz = num ** 0.5
    print(f'A raiz do número digitado é {raiz:.2f}')
