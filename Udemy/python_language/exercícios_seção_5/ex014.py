"""
A nota final de um estudante é cauculada a partir de três notas atribuidas entre o intervalo de 0 a 10, respectiva-
mente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das tres notas mencionadas anteriormente obedece aos pesos: trabalho de laboratório peso 2; avaliação semestral peso 3; exame final peso 5. De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2.9), de recuperação (entre 3 e 4.9) ou se foi aprovado, faça todas as verificações necessárias.
"""
import sys

tr = float(input('Digite a nota do trabalho: '))
av = float(input('Digite a nota da avaliação: '))
exf = float(input('Digite a nota do exame final: '))

if (tr > 10 or tr < 0) or (av > 10 or av < 0) or (exf > 10 or exf < 0):
        print('ALGUMA NOTA DIGITADA É INVALIDA')
        sys.exit()


tr = tr * 0.2
av = av * 0.3
exf = exf * 0.5

m = tr + av + exf


if m < 3:
    print(f'MÉDIA INSUFICIENTE [{m:.2f}]')
    print('VOCÊ FOI REPROVADO')
elif (m >= 3) and (m < 5):
    print(f'SUA MÉDIA FOI DE [{m:.2F}]')
    print('VOCÊ ESTÁ DE RECUPERAÇÃO')
else:
    print(f'PARABÉMS!!!!  COM A MÉDIA [{m:.2f}] VOCÊ FOI APROVADO!!!!')


