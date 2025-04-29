"""
Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor.
para caucular a comissão, considere a tabela abaixo
-----------------------------------------------------------------------------------
              Venda mensal                              |        Comissão
--------------------------------------------------------|--------------------------
Maior ou igual a R$1000.000.00                          | R$700.00 + 16% das vendas
--------------------------------------------------------|--------------------------
Menor que R$ 100.000.00 e maior ou igual a R$80.000.00  | R$650.00 + 14% das vendas
--------------------------------------------------------|--------------------------
Menor que R$ 80.000.00 e maior ou igual a R$60.000.00   | R$600.00 + 14% das vendas
--------------------------------------------------------|--------------------------
Menor que R$ 60.000.00 e maior ou igual a R$40.000.00   | R$550.00 + 14% das vendas
--------------------------------------------------------|--------------------------
Menor que R$ 40.000.00 e maior ou igual a R$20.000.00   | R$500.00 + 14% das vendas
--------------------------------------------------------|--------------------------
Menor que R$ 20.000.00                                  | R$400.00 + 14% das vendas
-----------------------------------------------------------------------------------
"""
totvenda = float(input('Digite o valor total de vendas '))

if totvenda < 20_000:
    comissao = totvenda * .14 + 400 
elif totvenda >= 20_000 and totvenda < 40_000:
    comissao = totvenda * .14 + 500 
elif totvenda >= 40_000 and totvenda < 60_000:
    comissao = totvenda * .14 + 550 
elif totvenda >= 60_000 and totvenda < 80_000:
    comissao = totvenda * .14 + 600 
elif totvenda >= 80_000 and totvenda < 100_000:
    comissao = totvenda * .14 + 650 
elif totvenda >= 100_000:
    comissao = totvenda * .16 + 700 
    
print(f'A comissão do vendedor será de {comissao:.2f}')