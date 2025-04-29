"""
Faça um programa que leia a altura e o sexo de uma pessoa e caucule e mostre seu peso ideal
utilize as seguintes formulas (onde h corresponde à altura ):
 - homens: (72.7 * h) - 58
 - mulheres: (62.1 * h) - 44.7
"""
sex = input('Tecle  [H] Homen   [M] Mulher: ').lower()
if sex == 'h':
    print('      Peso ideal para Homens      ')
    h = float(input('Digite a altura: '))
    ide = (72.7 * h) - 58
    print(f'O seu peso ideal é {ide:.2f}')
else:
    print('      Peso ideal para Mulheres      ')
    h = float(input('Digite a altura: '))
    ide = (62.1 * h) - 44.7
    print(f'O seu peso ideal é {ide:.2f}')
