"""
Escreva um programa de ajuda para vendedores. A partir de um total lido mostre:
- Total a pagar com 10% de desconto
- O valor de cada parcela no parcelamento em 3x sem juros
- A comissão do vendedor, no caso da comição ser a vista ( 5% do valor total)
"""
tpg = float(input('Digite o valor do produto: '))
des = tpg - (tpg * 0.1)
par = tpg / 3
co = des * 0.05
print(f'Total a pagar co 10% de desconto: {des}')
print(f'Em 3x de {par:.2f}')
print(f'Comissão para pg a vista: {co}')
