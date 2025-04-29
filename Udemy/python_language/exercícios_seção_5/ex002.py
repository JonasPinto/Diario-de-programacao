"""
Leia um número fornecido pelo usuário. Se esse número for positivo, caucule a raiz quadrada do número. Se o número
for negativo, mostre uma mensagem dizendo que o número é inválido.
"""
num = float(input('Digite um número: '))
if num < 0:
    print('O número é invalido')
else:
    raiz = num ** (1/2)
    print(f'A raiz quadrada do número {num} é {raiz:.2f}')
