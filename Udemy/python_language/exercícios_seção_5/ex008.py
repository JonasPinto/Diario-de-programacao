"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba ma tela a média destas notas
Uma nota valida deve ser, obrigatóriamente, um valor entre 0.0 e 10.0, onde caso não possua um valor válido, este
fato deve ser informado ao usuário e o programa termina.
"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
if nota1 < 0 or nota1 > 10:
    print('INVALID INPUT')
elif nota2 < 0 or nota2 > 10:
    print('INVALID INPUT')
else:
    media = (nota1 + nota2) / 2
    print(f'MÈDIA = {media:.1f}')

