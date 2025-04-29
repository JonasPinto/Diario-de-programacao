"""
Loop while
Forma geral
While expressão_booleana:   -> enquanto
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

# Exemplo 1
numero = 0
while numero < 11:
    print(numero, end=' ')
    numero = numero + 1

# OBS: em um loop while é importante que cuidemos do criterio de parada para não causar loop infnito

# Exemplo 2

resposta = ''
while resposta != 's':
    resposta = input('Já terminou ? S/N')


                    # c ou java

while (expressão){                   do {
    //Execução                           //Execução
}                                    }while(expressão)

"""


