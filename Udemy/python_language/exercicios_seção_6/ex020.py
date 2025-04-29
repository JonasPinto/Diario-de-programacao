'''Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número de dados lidos e número de valores pares. O processo termina quando for digitado o número 1000. '''

from typing import List

dl, np = [], []
fim, cont, nvp, nvl = 0, 0, 0, 0

while fim != 1000:
    dl.append(int(input('Digite um número ')))
    nvl = nvl + 1
    fim = dl[cont]
    if dl[cont] % 2 == 0:
        np.append(dl[cont])
        nvp = nvp + 1
    else:
        print('O número digitado é impar')
    cont =  cont + 1

print(f'Foram digitados {nvl} valores\n{nvp} números são pares\nOs números pares digitados são = {np}')