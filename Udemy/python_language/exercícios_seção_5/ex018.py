""" Faça um programa que mostre ao usúario um menu com 4 opções de operações matematicas. O usúario escolhe uma
das opções e oseu programa então pede dois valores numéricos e realiza a operação, mostra o resultado e sai.
"""
print('****************************************************')
print('           OPERAÇÕES MATEMÁTICAS                    ')
print('****************************************************')
print('\n\nESCOLHA UMA OPÇÃO A BAIXO\n[1] Soma\n[2] Subtração\n[3] Divisão\n[4] Multiplicação')
op = int(input())

if op == 1:
    print('FUNÇÂO SOMA')
    print('\nDigite dois números para serem somados')
    n1 = float(input())
    n2 = float(input())
    r = n1 + n2
    print(f'A soma de {n1} + {n2} é = {r}')
elif op == 2:
    print('FUNÇÃO SUBTRAÇÃO')
    print('\nDigite dois números para sere subtraidos')
    n1 = float(input())
    n2 = float(input())
    r = n1 - n2
    print(f'{n1} - {n2} é = {r}')
elif op == 3:
    print('FUNÇÂO DIVISÂO')
    print('\nDigite dois números para serem divididos')
    n1 = float(input('Dvidendo '))
    n2 = float(input('Divisor '))
    r = n1 / n2
    print(f'{n1} dividido por {n2} é = {r}')
elif op == 4:
    print('FUNÇÃO MULTIPLICAÇÃO')
    print('Digite dois números para serem multiplicados')
    n1 = float(input())
    n2 = float(input())
    r = n1 * n2
    print(f'{n1} x {n2} é = {r}')
else:
    print('OPÇÃO INVALIDA')



