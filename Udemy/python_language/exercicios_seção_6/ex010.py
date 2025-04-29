'''
Faça um programa que caucule e mostre a soma dos 50 primeiros números pares
'''
t = 0
for n in range(51):
    if n % 2 == 0:
        t += n
print(f'A soma de todos os pares de 0 á 50 é = {t}')
