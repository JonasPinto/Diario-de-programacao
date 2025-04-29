'''Escreva um algoritimo que leia um número inteiro entre  100 e 999 e imprima na saída cada um dos algarismos que compõem o número'''

n = int(input('Digite um mnúmero entre 100  e 999 '))
if n >= 100 and n < 1000:
    st = str(n)
    for i in range(len(st)):
        print(f'{i + 1}° algarismo = {st[i]}')
else:
    print('Número inválido')