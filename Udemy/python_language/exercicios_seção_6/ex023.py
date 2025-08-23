"""
Faça um algoritmo que leia um número positivo e emprima seus divisores
"""
# Algoritmo para ler um número positivo e imprimir seus divisores

# Lê o número
n = int(input("Digite um número positivo: "))

if n > 0:
    print(f"Divisores de {n}:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
else:
    print("Por favor, digite um número positivo ")
