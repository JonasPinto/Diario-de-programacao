# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.from math 

from math import trunc

numero = float((input("Digite um número real: ")).replace(',','.'))
print(type(numero))
print(f"A porção inteira de {numero} é {trunc(numero)}.")
