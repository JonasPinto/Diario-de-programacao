# faça a leitura de tres valores e apresente como resultado a soma dos quadrados dos tres valores

n1 = float(input(f'Digite o 1° valor: '))
n2 = float(input(f'Digite o 2° valor: '))
n3 = float(input(f'Digite o 3° valor: '))
s = (n1 * n1) + (n2 * n2) + (n3 * n3)
print(f'A soma dos quadrados dos numeros digitados é \033[31m{s:.2f}')

