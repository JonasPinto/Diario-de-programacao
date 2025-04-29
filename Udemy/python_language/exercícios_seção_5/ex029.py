# Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100. Eescolha números aleatórios entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b, onde a e b são números aleatórios. Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas, além de quantas vezes o aluno acertou.

from random import randint

list_in = [] # lista de entrada
list_out_a = [] # lista de saida a
list_out_b = [] # lista de saida b
list_r = [] # lista de respostas
i = 1 # variavel de controle para o laço for
r_ok = 0 # quantidade de respostas corretas
r_err = 0 # quntidade de respostas incorretas

for i in range (0, 5): 
    a = randint(1, 10) # atribui números aleatórios as variaveis a e b
    b = randint(1, 10)       
    print(f'Pergunta: Qual é a soma de {a} + {b} ?') # mostra a pergunta com números aleatórios 
    list_in.append(input('Resposta: ')) # guarda as respostas de entrada do usuario
    list_out_a.append(a) # o número aleatorio gerado é guardado na lista de saída a e b
    list_out_b.append(b)
    list_r.append(a + b) # executa a soma entre a e b a guarda o resultado na lista de resposta

for i in range(0,5):
    print(f'\nA soma de {list_out_a[i]} + {list_out_b[i]} = {list_r[i]}')
    if list_in[i] == str(list_r[i]):
        print(f'Sua resposta = {list_in[i]}') # faz comparação entre a soma gerada e o resultado, se verdadeiro (r_ok -> resposta correta) recebe + 1  se nao (r_err -> resposta errada recebe + 1)
        print(f'Resposta correta\n')
        r_ok += 1
    else:
        print(f'Sua resposta = {list_in[i]}')
        print(f'Resposta incorreta\n')
        r_err += 1
print(f'Acertos = {r_ok} questões\nErros = {r_err} questões') # mostra na tela quantas respostas foram corretas e quantas foram incorretas