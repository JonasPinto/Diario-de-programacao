# Usando switch (if, else e elif em python) escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
# da semana correspondente a esse número.

num = int(input('Digite um número: '))

if num == 1:
    print(f'O número {num} corresponde a Domingo')
elif num == 2:
    print(f'O número {num} corresponde a Segunda feira')
elif num == 3:
    print(f'O numero {num} corresponde a terça feira')
elif num == 4:
    print(f'O número {num} corresponde a quarta feira')
elif num == 5:
    print(f'O número {num} corresponde a quinta feira')
elif num == 6:
    print(f'O número {num} corresponde a sexta feira')
else:
    print(f'O número {num} corresponde a sábado')
