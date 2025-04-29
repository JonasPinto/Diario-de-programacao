# Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³. M = L / 1000

l = float(input('Digite o volume em litros: '))
m3 = l /1000
print(f'\033[34m{l}\033[m Litros são \033[34m{m3}M³\033[m')
