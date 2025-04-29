# Leia um ângulo em graus e apresente-o convertido em radianos R = G * PI / 180


from math import pi

g = float(input('Digite o angulo para ser convertido em radianos: '))
r = (g * pi) / 180
print(f'\033[31m{g}°\033[m graus correspondem a \033[31m{r:.2f}\033[m radianos')
