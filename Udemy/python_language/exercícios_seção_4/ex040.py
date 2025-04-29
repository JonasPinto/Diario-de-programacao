""" Uma empresa contrata um encanador a R$ 30 por dia, faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que devera ser paga
ao trabalhador, sabendo-se que 8% são descontados par o imposto de renda.
"""
dt = int(input('Digite quantos dias foram tarbalhados: '))
dtt = dt * 30
print(f'Você recebera R$ \033[32m{dtt - (dtt * 0.08)}\033[m')

print(f'\033[36m8%\033[m Equivalente a R$ \033[32m{dtt * 0.08:.2f}\033[m sera descontado para o imposto de renda')
