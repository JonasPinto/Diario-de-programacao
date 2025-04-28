 # Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa

from math import hypot

cateto_oposto = float(input('Comprimento do cateto oposto: ').replace(',', '.'))
cateto_adjacente = float(input('Comprimento do cateto adjacente: ').replace(',', '.'))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'Hipotenusa {hipotenusa:.2f}')