"""
Faça um programa para verificar se um determinado número inteiro é divisivel por 3 ou 5, mas não
simultaneamente pelo dois.
"""
n = int(input('Digite o número para verificação: '))

if (n % 3 == 0) and (n % 5 == 0):
    print(f'O número {n} é divisivel por 3 e por 5')
elif n % 3 == 0:
    print('O número digitado é divisivel apenas por 3')
elif n % 5 == 0:
    print('O número digitado apenas é divisivel por 5')
else:
    print('O número digitado nao pode ser dividido por 3 ou por 5 sem que o resto seja 0')

