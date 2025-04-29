# Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o número ao quadrado

num = float(input('Digite um número real: '))
if num > 0:
    raiz = num ** (1/2)
    print(f'A raiz do número {num} é {raiz:.2f}')
else:
    qua = num ** 2
    print(f'O número {num}² é = a {-qua}')
