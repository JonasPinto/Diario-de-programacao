# Faça um programa que receba trêz números e mostre-os em ordem crescente.

lista = []

for _ in range(3):
    n = int(input('Digite um número: '))
    lista.append(n)
lista.sort()
print(f'Assim ficam os números em ordem crescente -> {lista}')

