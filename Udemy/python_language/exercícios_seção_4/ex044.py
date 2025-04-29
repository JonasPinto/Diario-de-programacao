"""
Receba a altura de um degrau de uma escada e a altura que o úsuario deseja alcançar subindo a escada
caucule e mostre quantos degraus o usuario deverá subir para atingir seu objetivo.
"""
print('DIGITE AS MEDIDAS EM CENTIMETRO CM')
h = float(input('Digite a altura do degrau: '))
qtd = float(input('Informe a altura que deseja alcançar: '))
totd = qtd / h
print(f'Para chegar a {qtd} CM de altura suba {totd:.1f} degraus')
