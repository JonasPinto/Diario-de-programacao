# Leia um valor em R$ real e a cotação do dolar, mostre o valor de rais convertido em dolar.

r = float(input('Informe quantos reais deseja converter para dolar: '))
co = float(input('Informe a cotação atual do dolar: '))
d = r / co
print(f'R${r} reais equivalem a US${d} dolares')