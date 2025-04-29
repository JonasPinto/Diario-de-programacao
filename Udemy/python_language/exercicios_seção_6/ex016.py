'''Faça um programa que leia um número inteiro positivo impar N e imprima todos os números impares de 1 até N em ordem decrescente'''


try:
    n = int(input('Digite um número positivo impar  '))
    for i in range(n, -1, -2):
        print(i, end=' ')

except:
    print('Letras são inválidas')
