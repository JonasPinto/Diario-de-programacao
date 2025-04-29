'''
Faça um programa que leia um número inteiro N e depois mostre os primeiros N números naturais ímpares
'''
import time

num = int(input('Digite um número natural: '))

for n in range(1, num + 1):
    if n % 2 != 0:
        time.sleep(0.2)
        print(n ,end=' ')