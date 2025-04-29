"""
Leia a nota e o número de faltas de um aluno, e esreva seu conceito. De acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito

NOTA          CONCEITO(ATÉ 20 FALTAS)   CONCEITO(MAIS DE 20 FALTAS)
9.0 ATÉ 10.0             A                            B
7.5 ATÉ 8.9              B                            C
5.0 ATÉ 7.4              C                            D
4.0 ATÉ 4.9              D                            E
0.0 ATÉ 3.9              E                            E
"""
import os
nota = float(input('Digite a sua nota: '))
faltas = int(input('Digite a quantidade de faltas: '))
conceito = ''
if faltas <= 20:
    if nota < 4:
        conceito = 'E'
    elif nota >= 4 and nota <= 4.9:
        conceito = 'D'
    elif nota >= 5 and nota <= 7.4:
        conceito = 'C'
    elif nota >= 7.5 and nota <= 8.9:
        conceito = 'B'
    elif nota >= 9.0 and nota <= 10:
        conceito = 'A'
elif faltas > 20:
    if nota < 5:
        conceito = 'E'
    elif nota >= 5 and nota < 7.5:
        conceito = 'D'
    elif nota >= 7.5 and nota < 9:
        conceito = 'C'
    elif nota >= 9 and nota <= 10:
        conceito = 'B'
if nota > 10 or nota < 0:
    print('NOTA INVALIDA')
else:
    print(f'Conceito {conceito}')


