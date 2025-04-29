"""
Leia a distância em km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule
o consumo em km/l e escreva uma mensagem de acordo com a tabela abaixo:
CONSUMO    /   KM/L  / MENSAGEM
menor que  /    8    / venda o carro!
entre      / 8  e 14 / Econômico
maior que  /   12    / Super econômico
"""
d = float(input('Digite a distância em km: '))
g = float(input('Digite a quantiadde de combustivel gasto: '))

cons = d / g

if cons < 8:
    print('Venda o carro!')
elif (cons >= 8) and (cons <= 12):
    print('Econômico!')
elif cons > 12:
    print('Super econômico!')



