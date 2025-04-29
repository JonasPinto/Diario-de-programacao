# Leia um número inteiro e imprima a soma do sucessor do seu triplo com o antecessor de seu dobro

n = int(input('Digite um numero: '))
s = ((n * 3) + 1) + ((n * 2) - 1)
print(f'A soma do sucessor do triplo de {n} + o antecessor de seu dobro é = {s}')
