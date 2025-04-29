'''
Faça um programa que leia 10 números inteiros e imprima sua média
'''
num = []
for i in range(1,11):
    num.append(int(input(f'Digite o {i}° número: ')))

print(num,f'\n A média dos números digitados é = \033[32m{sum(num) / 10}\033[m')
