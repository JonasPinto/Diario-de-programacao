'''
Faça um programa que escreva na tela de 1 até 100, de 1 em 1, 3 vezes. Aprimeira vez usando a estrutura de repetição for, a segunda utilizando while.
'''

for n in range(1, 101):
    print(n,end=' ')

print('\n')

n = 0
while n < 100:
    n = n + 1
    print(n,end=' ')

