'''
Definição de funções
  - Funções são pequenas partes de codigo que realizão tarefas especificas
  - Pode ou não receber e retornar dados de entreda ou saída
  - Muito uteis para executar determinadas tarafas que se repetirão no codigo

OBS: ao criar uma função devese evitar que a mesma realize varios procedimentos, devemos criar funções que realizam poucas tarefas, funções devem ser simples.

No python existem diversas funções internas já prontas para uso, são as chamadas (Built-in Functions)
ou Funções integradas.

Acessando o link abaixo podemos ver todas as funções internas do python
     [https://docs.python.org/3.8/library/functions.html]

 DRY - Dont' Repeat Yourself  - Não repita você mesmo / Não repita seu código
'''
# Definindo funções:

# def nome_da_função(parametros_de_entrada):
  # bloco_da_função

'''
Importante: 
(Nome da função) -> sempre com letras minusculas, e se for nome composto , separado por underline(snap case)

(parametros de entrada) -> Opcionais, separados por virgula

(Bloco da função) -> Também chamado de corpo da função, é onde o processamento da função acontece, nessa parte pode ou não ter o retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao python que estamos definindo uma função, Também abrimos o bloco de cóidigo com o já conhecido dois pontos: que é utilizado em python para definir blocos.
'''
# Definindo a primeira função 

def diz_oi():
  print('oi!')

'''
OBS:
1 - Veja que, dentro das nossas funções podemos utilizar outras funções
2 - Veja que nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer oi
3 - Veja que esta função não recebe nenhum parâmetro de entrada
4 - Veja que esta função não tem retorno
'''
# Utilizando as funções 
# Para utilizar uma função, deve-se chamar a mesma

diz_oi() # Ao chamar a função criada ela traz a tona os comandos do bloco de intruções, executando-os como foram implementados

def tabuada_2():
  for i in range(10):
    print(f'2 x {i} = {i * 2}')
    

tabuada_2()
