"""
Determine se um ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400 ou se for divisível por
4 e não for divisível por 100
"""
ano = int(input('Digite o ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('O ano digitado é Bissexto')
else:
    print('O ano digitado não é Bissexto')
