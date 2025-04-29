'''Faça um programa que receba dois números. Caucule e mostre:
1 a soma dos números pares desse intervalo de números, incluindo os números digitados 
2 a multiplicação dos números ímpares desse intervalo, incluindo os digitados'''

n1 = int(input('Digite o primeiro número '))
n2 = int(input('Digite o segundo número '))
s = 0
m = 1
if n1 > n2:
    maior = n1
    n1 = n2
    n2 = maior
    
for i in range(n1, n2 + 1):
    if i % 2 == 0:
        s = s + i
    else:
        m = m * i


print(f'A soma dos números pares do intervalo é = {s} \nA multiplicação dos números inpares do intervalo é  = {m} ')
