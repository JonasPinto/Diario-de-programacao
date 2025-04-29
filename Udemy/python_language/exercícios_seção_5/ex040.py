'''
O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos. A comissão e os impostos são cauculados sobre o custo de fabrica, de acordo com a tabela abaixo. Leia o custo de fabrica e escreva o custo ao consumidor.

custo de fabrica            /   % do distribuidor   /   % dos impostos 

até R$ 12000,00                         5                  insento
entre R$ 12000,00 e 25000,00           10                     15
acima de R$ 25000,00                   15                     20
'''
custo_fabrica = float(input('Digite o custo de fabrica do veiculo: '))
custo_total = 0

if custo_fabrica > 0 and custo_fabrica <= 12000 :
   custo_total = custo_fabrica + (custo_fabrica * 0.05)

if custo_fabrica > 12000 and custo_fabrica <= 25000 :
   custo_total = custo_fabrica + (custo_fabrica * 0.25)

if custo_fabrica > 25000 :
   custo_total = custo_fabrica + (custo_fabrica * 0.35)

print(f'O custo total do veiculo será de R$ {custo_total}')