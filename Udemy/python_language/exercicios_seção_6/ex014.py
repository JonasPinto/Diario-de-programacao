'''
Faça um programa que leia um número inteiro positivo par N, e imprima todos os números pares de 0 até N em ordem decrescente
'''
from time import sleep
while True:
    try:
        n = int(input('Digite um número inteiro positivo par  '))
        if n > 0 and n % 2 == 0:
            for i in range(n, -2, -2):
                sleep(0.2)
                print(i, end= ' ')
        else:
            print('Números impares não são validos!')
    except:
        print('Letras não são validas!')        
    resp = input('\n ENTER -> Continuar \n S     -> Sair ')
    if resp == 's':
        break
        