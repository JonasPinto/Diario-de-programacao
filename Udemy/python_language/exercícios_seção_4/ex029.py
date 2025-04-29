# Leia quatro notas caucule a média aritimetica e mostre-a na tela para o usuario.

n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
n3 = float(input('Digite a 3º nota: '))
n4 = float(input('Digite a 4º nota: '))
m = (n1 + n2 + n3 + n4) / 4
print(f'A média entre as 4 notas é de \033[31m{m:.2f}\033[m')
