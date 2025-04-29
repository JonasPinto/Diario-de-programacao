# Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente ao número.

n = int(input('Digite um número para saber o mes correspondente: '))
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

print(f'O número {n} corresponde ao mês de {meses[n - 1]}')
