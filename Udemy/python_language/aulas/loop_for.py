"""
Loop for
loop -> Estrutura de repetição
for -> uma dessas estruturas

c ou java
for(int i = 0; i < 10; i++){
   //execução do loop
}

utilizamos loops para iterar sobre sequências ou valores iteráveis
exemplos de iteraveis:
- string  -> 'jonas da silva pinto
- lista   -> [1, 2, 3, 4, 34, 33]
- range   -> numeros = range(1, 10)

nome = 'jonas da silva pinto'
lista = [1, 3, 5, 7, 9]
numero = range(1, 10)

# exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra, end = '')  -> end = '' imprime na mesma linha

# exemplo de for 2 (iterando em uma lista)
for numero in lista:
    print(numero)

# exemplo de for 3 (iterando sobre um range)

range(1, 10) -> do 1 até o 9
1, 2, 3, 4, 5, 6, 7, 8, 9 o n°10 nao é incluso

nome = 'jonas da silva pinto'
lista = [1, 3, 5, 7, 9]
numero = range(1, 10)


for numero in range(1, 10):
    print(numero)

Enumerate: # o enumerate traz 2 parametros (o indice e o conteudo da variavel
((0, 'j'), (1, 'o'), (2, 'n'), (3, 'a'), (4, 's').....)
for indice, letra in enumerate(nome):
    print(indice, letra)

for indice, letras in enumerate(nome):
    print(letras)

for _, letras in nome:      # utiliza-se o underline para descartar o indice
    print(letras)

for indice, letras in enumerate(nome):  # significa (para indice e letras dentro da variavel (nome)
# nesse caso pode-se printar apenas o indice ou apenas as letras ou os dois
    print(indice)

qtd = int(input('Quantas vezes esse loop deve rodar'))
for n in range(1, qtd + 1):  # range significa alcance
# sempre utilizar + 1 pois o range alcança o valor passado -1
    print(f'Imprimindo \033[31m{n}\033[m')

tabela de emojis unicode: http://apps.timwhitlock.info/emoji/tables/unicode
"""
qtd = int(input('Quantos números deseja somar ?  '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'{n}° valor de {qtd}: '))
    soma += num
print(f'A soma entre todos os numero digitados é \033[31m{soma}\033[m')

for _ in range(3):
    for i in range(1, 11):
        print('\U0001F60D' * i)
