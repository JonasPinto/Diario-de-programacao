'''
Faça um algoritimo utilizando o comando while que mostra uma contagem regressiva na tela, iniciando em 10 e terminando em 0. mostrar uma mensagem  "FIM" após a contagem.
'''
import time

var = 10

print('Contando......')

while var > -1:
    print(var,end=' ')
    var = var - 1
    time.sleep(1)

print('\n"FIM"')