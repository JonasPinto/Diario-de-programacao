'''
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')


OBS: Em python, quando uma função não retorna nenhum valor, o retorno é none

OBS: Funções python que retornam valores, devem retornar estes valores com a palavra reservada return

OBS: Não presisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução da função para outras funções.

# Exemplo de uma função  com retorno

def quadrado_de_7():
    return 7 * 7

# A mesma função com uma variavel recebendo o retorno
ret = quadrado_de_7()
print(f'Retorno {ret}') Resultado -> Retorno 49

# A mesma função sem uma variavel 
print(f'Retorno {quadrado_de_7()}') Resultado -> Retorno 49


alguem = 'Jonas'


def diz_oi():
    print('oi')

print(diz_oi + alguem)
    print(diz_oi + alguem)

TypeError: unsupported operand type(s) for +: 'function' and 'str'


def diz_oi():
    return 'oi'

print(diz_oi() + alguem) # dessa maneira podemos concatenar a função com uma variável

obs: Sobre a palavra reservada return

1 - O return finaliza a função, ou seja, ela sai de execução depois do return
2 - Podemos ter, em uma função, diferentes returns
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores

# Exemplo 1 - O return finaliza a função, ou seja, ela sai de execução depois do return
def parabens():
    print('Esse print está sendo executado') # antes do return é executado 
    return 'Parabens'
    print('Esse print não é executado') # Após o return não é executado

print(parabens()) 


# exemplo 2 - Podemos ter, em uma função, diferentes returns
def nova_função():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_função())


# Exemplo 3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores

def outra_função():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_função()

print(num1, num2, num3, num4)



'''



from random import randint, random

# Criando uma função para jogar moeda

def joga_moeda():
    if random() > 0.5:  # gera um numero pseudo-randômico entre 0 e 1
        return 'Cara'
    return 'Coroa'

print(joga_moeda())


def par_ou_impar():
    numero = randint(1, 1000) # Gera um número aleatorio entre 1, 1000
    if numero % 2 == 0:
        return 'Par'
    return 'Impar' 

print(f'O número que eu escolhido é {par_ou_impar()}')