# Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. L = 1000 * m

m3 = float(input('Digite o volume cubico: '))
l = m3 * 1000
print(f'\033[32m{m3}M³\033[m são equivalentes a \033[32m{l:.2f}\033[m Litros')

