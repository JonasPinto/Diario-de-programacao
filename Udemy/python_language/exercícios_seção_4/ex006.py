# Leia uma temperatura em graus Celsius e apresente-a convertida em graus fahrenheit. F = C * (9.0/5.0) + 32.0

c = float(input('Digite a temperatura em graus c° Celcius: '))
f = (c * 1.8) + 32
print(f'{c}° graus Ceucius são {f}° graus fahrenheit')