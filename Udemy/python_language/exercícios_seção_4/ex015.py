# Leia um ângulo em radianos e apresente-o convertido em graus G = R * 180 / PI

from math import pi

r = float(input('Digite o valor em radianos: '))
g = r * 180 / pi
print(f'\033[36m{r}\033[m radianos são \033[36m{g:.2f}°\033[m graus')
