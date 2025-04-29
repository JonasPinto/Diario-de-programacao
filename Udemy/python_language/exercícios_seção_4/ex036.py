# Leia a altura e o raio de um cilindro e mostre o volume V = pi * r² * h

h = float(input('Digite a altura do cilindro: '))
r = float(input('Digite o raio do cilindro: '))
v = 3.1416 * (r**2) * h
print(f'O volume do cilindro é de \033[35m{v:.2f}\033[m')