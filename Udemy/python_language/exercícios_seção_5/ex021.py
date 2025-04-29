"""
Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva uma mesnsagen de erro
se opção for iválida.
"""
import os
op = ''
while op != 's':
    print('\n\nESCOLHA UMA OPÇÃO OU DIGITE S PARA SAIR:\n')
    print('[1] Soma de 2 números')
    print('[2] Diferença entre dois números (maior pelo menor)')
    print('[3] Multiplicação entre 2 números')
    print('[4] Divisão entre 2 números')
    op = input('')
    if op == '1':
        print('SOMA DE DOIS NÚMEROS')
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        print(f'A soma dos dois números é = {sum([n1, n2])}')
        os.system('pause')
    elif op == '2':
        print('DIFERENÇA ENTRE DOIS NÚMEROS')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        if n1 > n2:
            n1 = n1
            n2 = n2
        else:
            m = n2
            n2 = n1
            n1 = m
        dif = n1 - n2
        print(f'A diferença entre os dois numeros é = {dif}')
        os.system('pause')
    elif op == '3':
        print('MULTIPLICAÇÃO ENTRE DOIS NÚMEROS')
        n1 = float(input('Digite o 1° número: '))
        n2 = float(input('Digite o 2° número: '))
        x = n1 * n2
        print(f'{n1} X {n2} = {x:.2f}')
        os.system('pause')
    elif op == '4':
        print('DIVISÃO ENTRE DOIS NÚMEROS')
        n1 = float(input('Digite o dividendo: '))
        n2 = float(input('Digite o divisor: '))
        if n2 == 0:
            print('O DENOMINADOR NÃO PODE SER 0')
            os.system('pause')
        else:
            div = n1 / n2
        print(f'{n1} dividido por {n2} = {div:.2f}')
        os.system('pause')
