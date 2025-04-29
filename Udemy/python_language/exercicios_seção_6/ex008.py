'''
Escreva um programa que leia 10 números e mostre o maior e o menor valor lido
'''
nums = []

for i in range(1,11): # Range -> Alcance
    nums.append(float(input(f'Digite o {i}° número: ')))

bigger = nums[0]
smaller = nums[0]

for i in range(len(nums)):
    if nums[i] > bigger:
        bigger = nums[i]
    if nums[i] < smaller:
        smaller = nums[i] 

print(f'O maior número lido foi o -> {bigger}\nO menor número lido foi o -> {smaller} ')