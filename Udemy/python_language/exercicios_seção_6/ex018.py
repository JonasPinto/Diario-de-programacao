'''Escreva um algoritimo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário'''

qtn = int(input('Informe quantos números vão ser digitados '))
ne = []
maior = 0
cont = 0
seq = 1
while qtn >= 1:
    ne.append(int(input(f'Digite o {seq}° número ')))
    if ne[cont] > maior:
        maior = ne[cont]
    cont = cont + 1    
    qtn = qtn - 1
    seq = seq + 1
print(f'O maior número foi o {maior}\nO número {maior} foi digitado {ne.count(maior)} x')   
    

