"""
Tres amigos jogaram na loteria. Caso eles ganhem, o prêmio devera ser repartido proporcionalmente conforme cada um
investiu.
Faça um programa que leia qunto cada um investiu, o valor do premio e quanto cada um recebera conforme o investimento
feito
"""
vp = float(input('Qual o valor do prêmio: '))

print('\nDigite abaixo o valor que cada jogador investiu')
j1 = float(input('Jogador 1: '))
j2 = float(input('Jogador 2: '))
j3 = float(input('Jogador 3: '))

tot = j1 + j2 + j3

porj1 = (j1 / tot) * 100
porj2 = (j2 / tot) * 100
porj3 = (j3 / tot) * 100

prej1 = (porj1 * vp) / 100
prej2 = (porj2 * vp) / 100
prej3 = (porj3 * vp) / 100

print(f'Jogador 1 investiu R${j1:.2f} e recebera {prej1:.2f} proporcional a {porj1:.2f}% da aposta')
print(f'Jogador 2 investiu R${j2:.2f} e recebera {prej2:.2f} proporcional a {porj2:.2f}% da aposta')
print(f'Jogador 3 investiu R${j3:.2f} e recebera {prej3:.2f} proporcional a {porj3:.2f}% da aposta')


