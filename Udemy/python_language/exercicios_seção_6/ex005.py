'''
Faça um programa que peça ao usuário para digitar 10 valores e some-os.
'''

nums = []
for num in range(0, 10):
    nums.append(int(input('Digite um número para ser somado: ')))

print(nums)
print(f'A soma de todos os números digitadods é = {sum(nums)}')