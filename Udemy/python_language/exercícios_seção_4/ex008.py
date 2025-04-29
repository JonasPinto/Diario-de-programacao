# Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. C = K – 273.15

k = float(input('Digite a tempratura em k° kelvin: '))
c = k - 273.15
print(f'{k}°kelvin são respectivamente {c:.2f}° celcius')
