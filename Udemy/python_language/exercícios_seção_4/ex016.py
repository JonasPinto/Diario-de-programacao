# Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros. C = P * 2.54

p = float(input('Digite o comprimento em polegadas: '))
c = p * 2.54
print(f'\033[32m{p}"\033[m polegadas são \033[32m{c}\033[m centimetros')
