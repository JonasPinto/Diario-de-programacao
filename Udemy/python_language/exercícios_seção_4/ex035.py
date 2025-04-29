# faça um programa que leia os catetos oposto e adjacente e mostre a hipotenuza


c1 = float(input('Didite o 1° cateto: '))
c2 = float(input('Digite o 2° cateto: '))
hip = ((c1 * c1) + (c2 * c2)) ** (1/2)
print(f'A hipotenuza desse triangulo coresponde a \033[31m{hip:.2f}\033[m')

