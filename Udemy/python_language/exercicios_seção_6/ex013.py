'''
Faça um programa que leia um número inteiro positivo par N, e imprima todos os números pares de 0 até N em ordem crescente
'''
from time import sleep
while True:
    n = int(input('Digite um número inteiro, positivo e par: '))
    if n > 0 and (n % 2 == 0):
        break
    else:
        print(f'O número {n} não é válido') 
for i in range(2, n + 1, 2):
    sleep(2)
    print(i , end=' ')  


