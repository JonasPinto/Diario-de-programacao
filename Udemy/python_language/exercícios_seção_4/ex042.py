"""
receba o salario base de um funcionario, caucule e imprima o salario a receber, sabendo-se que
esse funcionario tem uma gratificação de 5% e também é descontado 7% de imposto de renda
"""
slb = float(input('Digite o valor do salario base: '))
gr = slb * 0.05
des = (slb + gr) * 0.07
print(f'GRATIFICAÇÃO = R$ {gr}')
print(f'DESCONTO = R$ {des:.2f}')
print(f'A RECEBER = R$ \033[31m{(slb + gr) - des}\033[m')
