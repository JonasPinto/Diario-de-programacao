"""
faça um programa que leia o valor da hora em reais e a quantidade de horas trabalhadas
no mês, imprima o valor a ser pago ao funcionario adicionando 10% sobre o valor a ser cauculado
"""
vh = float(input('Digite o valor da hora: R$ '))
qht = float(input('Digite a quantidade de horas trabalhadas: '))
totr = (0.1 * (vh * qht)) + vh * qht
print(f'O total a receber é \033[31mR$ {totr}\033[m')
