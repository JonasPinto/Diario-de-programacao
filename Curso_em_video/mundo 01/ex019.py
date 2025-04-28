# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido

import random

nomes =[]

for i in range(1, 4 + 1):
    nome = input(f'Nome do {i}° aluno: ')
    nomes.append(nome)
    print(nomes)
    sorteado = random.choice(nomes)

print(f'\nO aluno sorteado foi {sorteado}')





