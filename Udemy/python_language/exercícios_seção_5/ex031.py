""" Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre qual a classificação dessa pessoa.
   Altura                        Peso
                   Menor 60   Entre 60 e 90   Acima de 90 
   menor que 1,20    A             D             G
   de 1,20 a 1,70    B             E             H
   maior que 1,70    C             F             I
"""
alt = float(input('Digite a sua altura: '))
pes = float(input('Digite o seu peso: '))

if alt < 1.20:
    if pes < 60:
        print('Classificação [ A ]')
    elif pes >= 60 and pes <= 90 :
        print('Classificação [ D ]')
    elif pes > 90:
        print('Classificação [ G ]')
elif alt >= 1.20 and alt <= 1.70:
    if pes < 60:
        print('Classificação [ B ]')
    elif pes >= 60 and pes <= 90:
        print('Classificação [ E ]')
    elif pes > 90:
        print('Classificação [ H ]')
elif alt > 1.70:
    if pes < 60:
        print('Classificação [ C ]')
    elif pes >= 60 and pes <= 90:
        print('Classificação [ F ]')
    elif pes > 90:
        print('Classificação [ I ]')
        
             