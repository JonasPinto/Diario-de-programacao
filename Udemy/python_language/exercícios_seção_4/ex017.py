# Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas. P = C / 2.54

c = float(input('Digite a medida em Cm (Centimetros): '))
p = c / 2.54
print(f'\033[31m{c}\033[m Cm são \033[31m{p:.2f}"\033[m Polegadas')

