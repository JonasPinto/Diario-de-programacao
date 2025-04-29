'''
Faça um programa que leia um número inteiro positivo impar N e imprima todos os números impares de 1 até N em ordem crescente
'''
from time import sleep
while True:
    try:
        n = int(input('Digite um número inteiro positivo impar  '))
        if n > 0 and n % 2 != 0:
            for i in range(1,n + 2,2):
                sleep(0.1)
                print(i,end=' ')
        else:
            print('Números pares não são validos!')
    except:
        print('Letras não são validas!')
    resp = input('\n ENTER -> Continuar \n S     -> Sair ')
    if resp == 's':
        break

