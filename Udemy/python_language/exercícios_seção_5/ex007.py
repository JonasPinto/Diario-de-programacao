# Faça um programa que receba dois números e mostre o maior. Se os dois números forem iguais, imprima (números iguais)
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
lista = [num1, num2]
if num1 == num2:
    print('Os números digitados são iguais')
else:

    print(f'O maior número digitado foi o {max(lista)}')

