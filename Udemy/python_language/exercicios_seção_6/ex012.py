'''
Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de N até 0 em ordem decrecente
'''
from time import sleep

n = int(input('Digite um número inteiro positivo: '))
for i in range(n, -1, -1):
    # sleep(0.1)
    print(i, end=' ')
    