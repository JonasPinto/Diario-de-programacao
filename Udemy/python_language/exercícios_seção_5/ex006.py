# Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles e a diferença entre ambos

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
maior = [num1, num2]
dif = max(maior) - min(maior)
print(f'O maior número digitado foi o {max(maior)} e a diferença entre els é de {dif}')
