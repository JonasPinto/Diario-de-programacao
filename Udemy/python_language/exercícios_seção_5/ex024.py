"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente
de imposto sobre o produto (MG 7 %; Sp 12 %; RJ 15 %; MS 8 %). Faça um programa em que o usúario entre com o valor
e o estado destino do produto e o programa retorne o preço final do produto acrecido do imposto do estado em que será
vendido. Se o estado digitado não for valido , mostrar uma mesnsagem de erro.
"""
import sys
vp = float(input('Digite o valor do produto: '))
es = input('Digite o nome ou sigla do estado onde será vendido o produto: ').lower()
tx = 0
if es == 'mg' or es == 'minas gerais':
    vp = vp + (vp * 0.07)
    tx = 7
elif es == 'sp' or es == 'são paulo':
    vp = vp + (vp * 0.12)
    tx = 12
elif es == 'rj' or es == 'rio de janeiro':
    vp = vp + (vp * 0.15)
    tx = 15
elif es == 'ms' or es == 'mato grosso do sul':
    vp = vp + (vp * 0.08)
    tx = 8
else:
    print('ERRO\n[1]VERIFIQUE SE DIGITOU UM ESTADO VALIDO\n[2]VERIFIQUE SE DIGITOU CORRETAMENTE')
    sys.exit()
print(f'O estado \033[31m{es}\033[m tem a taxa de \033[31m{tx}%\033[m \nO valor do produto com o imposto será de \033[31m{vp}\033[m')
