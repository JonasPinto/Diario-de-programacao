# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

nomes =[]

for i in range(1, 4 + 1):
    nome = input(f'Nome do {i}º aluno: ')
    nomes.append(nome)
    
shuffle(nomes)
print('A ordem de apresentação sera\n{}'.format(nomes))


