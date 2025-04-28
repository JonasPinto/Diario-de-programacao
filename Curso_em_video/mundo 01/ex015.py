#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print(f'_' * 40,'\n\n KM     = R$0,15\n', 'Diaria = R$60,00\n', '_' * 40)
qtd_km = float(input('\nInforme a quantidade de KM rodados: ').replace(',', '.')) * 0.15
qtd_dias = int(input('Informe a quantidade de dias de uso : ')) * 60
print(f'O Total a pagar é de R${qtd_km + qtd_dias:.2f}')

