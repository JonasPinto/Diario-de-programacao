# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

import time

r = float(input('Qantos reais voce tem na carteira : '))
d = r / 5.80
print('\n\nTROCANDO O DINHEIRO AGUARDE............... \n')
time.sleep(6)
print(f'Com ${r} reais você compra US${d:.2f} dolares')