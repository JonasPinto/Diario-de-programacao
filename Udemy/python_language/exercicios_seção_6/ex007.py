'''
Faça um programa que leia 10 números inteiros positivos, ignorando não positivos, e imprima sua média
'''
nums = []
cont = 1
num = 0
while cont <= 10:
    num = int(input(f'Digite o {cont}° número: '))
    if num < 0:
        print(f'O {cont}° número deve ser positivo')
        cont = cont
    else:
        nums.append(num)
        cont += 1

print(f'A média de todos os números digitados é = {sum(nums) / 10}')