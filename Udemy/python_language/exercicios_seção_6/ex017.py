'''Faça um programa que leia um número inteiro positivo N e calcule a soma dos N primeiros números naturais'''

try:
    ne = int(input('Digite um número inteiro positivo  '))
    s = []
    if ne >= 0:
        for i in range(ne, 0, -1):
            s.append(i)
        print(f'A soma de 0 até {ne} é = {sum(s)}')
    else:
        print('Não são permitidos números negativos')
except:
    print('Letras não são permitidas')
