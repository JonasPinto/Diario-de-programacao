# Leia uma distância em quilômetros e apresente-a convertida em milhas M = K / 1.61

km = float(input('Digite a distância em kilometros: '))
m = km / 1.6093
print(f'\033[31m{km}\033[m kilometros corespondem a \033[35m{m:.1f}\033[m milhas')
