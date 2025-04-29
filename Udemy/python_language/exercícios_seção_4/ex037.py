# Leia o salario atual e a %  que determinado funcionario obteve de aumento.

au = float(input('Digite a % de aumento: '))
sa = float(input('Digite o valor do salario atual: '))
sa = ((au / 100) * sa) + sa
print(f'O novo salario com aumento de {au}% é = \033[33mR${sa:.2f}\033[m')
