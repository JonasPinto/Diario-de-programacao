"""
Escreva um programa que receba um numero inteiro e escreva a soma de todos os divisores desse numero, com exceção dele proprio.
Ex: a soma dos divisores do numero 66 é 1+2+3+6+11+22+33 = 78
"""

n = int(input("Digite um numero: "))

s = 0
for i in range(1, n):
        if n % i == 0:
            s = s + i
            print(i)


print(f"A soma de todos os dividores de {n} é = {s}")