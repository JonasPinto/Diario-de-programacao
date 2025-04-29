"""
Faça um algoritmo que caucule a média ponderada das notas de 3 provas. A primeira e a segunda prova têm peso 1
e a terceira tem peso 2. Ao final mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para
aprovação deve ser superior a 60 pontos.
"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

m = (n1 + n2 + n3) / 3

if m > 60:
    print(f'A sua média foi {m:.2f} pontos')
    print('Você foi APROVADO!!!!!')
else:
    print(f'A sua média foi {m:.2f} pontos')
    print('Você foi REPROVADO')
