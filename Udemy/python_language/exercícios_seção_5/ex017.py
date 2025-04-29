# Faça um programa que caucule e mostre a area de um trapézio. A = ( Base maior + base menor) * altura
#                                                                                   2
print('Digite as medidas para calcular a area do trapézio')
bM = float(input('Digite a base maior: '))
bm = float(input('Digite a base menor: '))
al = float(input('Digite a altura: '))

a = ((bM + bm) * al) / 2

print(f'A area do trapézio é de {a}')
