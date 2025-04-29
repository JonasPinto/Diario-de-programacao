'''
Faça um algoritmo que caucule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:

          I M C            /      C l a s s i f i c a ç ã o
          <18,5                      Abaixo do peso
          18,6 - 24,9                Peso normal
          25,0 - 29,9                Sobrepeso
          30,0 - 34,9                Obesidade Grau I
          35,0 - 39,9                Obesidade Grau II(severa)
          >= 40,0                    Obesidade Grau III(mórbida)
'''
from math import pow

altura = (float(input('Digite a altura: ')))
peso = float(input('Digite o peso: '))

imc = peso / pow(altura, 2)
cla = ''

if imc < 18.5:
    cla = 'Abaixo do peso'
elif imc > 18.5 and imc <= 24.9:
    cla = 'com Peso normal' 
elif imc > 24.9 and imc <= 29.9:
    cla = 'com Sobrepeso'
elif imc > 29.9 and imc <= 34.9:
    cla = 'com Obesidade Grau I'
elif imc > 34.9 and imc <= 39.9:
    cla = 'com Obesidade Grau II (severa)'
elif imc >= 40:
    cla = 'com Obesidade grau III (mórbida)'
    

print(f'IMC = [{imc:.2f}]\nVocê está {cla} ')