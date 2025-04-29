# Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
# C = 5.0 * (F – 32.0) / 9.0

f = float(input('Digite a temperatura em f° fahrenheit: '))
c = 5 * (f - 32) / 9
print(f'{f}° graus fahrenheit são {c:.2f}° graus celcius')
