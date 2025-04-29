# Leia uma velocidade em KM/h (quilômetros por hora) e apresente-a convertida em M/S (metros por segundo).
# M = K / 3.6

print('--------------------------------')
print('    CONVERSOR DE KM/H PARA M/S    ')
print('--------------------------------')
k = float(input('Digite a velocidade em KM/H: '))
ms = k / 3.6
print(f'{k}km/h correspondem a \033[32m{ms:.2f}\033[m m/s')
