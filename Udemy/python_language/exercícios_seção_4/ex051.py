
# Escreva um programa que leia as coordenadas X e Y de pontos no R² e caucule sua distância da origem (0,0)

x = float(input('Entre com a medida do eixo X: '))
y = float(input('Entre com a medida do eixo Y: '))

d = ((x ** 2) + (y ** 2)) ** (1/2)

print(f'A partir da origem (x0, y0) a distância euclidiana é = {d:.3f} ')
