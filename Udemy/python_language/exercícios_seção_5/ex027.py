"""
Escreva um programa que dada a idade de um nadador, classifique-o em uma das seguintes categorias:
Ctegoria      /  idade
infantil A    /  5 a 7
infantil B    /  8 a 10
juvenil  A    /  11 a 13
juvenil  B    /  14 a 17
senior        /  maior de 18
"""
i = int(input('Digite a idade do nadador: '))

if i < 5:
    print('Idade insuficiente para competir')
elif (i >= 5) and (i <= 7):
    print(f'Com \033[31m{i}\033[m anos você se encaixa na categoria -> \033[31minfantil A\033[m')
elif (i >= 8) and (i <= 10):
    print(f'Com \033[31m{i}\033[m anos você se encaixa na categoria -> \033[31minfantil B\033[m')
elif (i >= 11) and (i <= 13):
    print(f'Com \033[31m{i}\033[m anos você se encaixa na categoria -> \033[31mjuvenil A\033[m')
elif (i >= 14) and (i <= 17):
    print(f'Com \033[31m{i}\033[m anos você se encaixa na categoria -> \033[31mjuvenil B\033[m')
elif i > 17:
    print(f'Com \033[31m{i}\033[m anos você se encaixa na categoria -> \033[31msenior\033[m')
