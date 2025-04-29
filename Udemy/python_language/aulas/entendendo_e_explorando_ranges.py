"""
Ranges
- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

formas gerais:

range(inicio, parada, passo):

OBS: valor de parada não inclusive (início padrão 0, e passo de 1 em 1)
# Forma 1
for num in range(11):
    print(num)

OBS: valor de parada não inclusive (início especificado pelo úsuario, e passo de 1 em 1)
# Forma 2
for num in range(1, 11):
    print(num)

OBS: valor de parada não inclusive (início especificado pelo úsuario, e passo especificado pelo usúario)
# Forma 3
for num in range(1, 10, 2):
    print(num)

OBS: valor de parada não inclusive (início especificado pelo úsuario, e passo especificado pelo usúario)
# Forma 4 (inversa)
for num in range(10, 0, - 1): inicio em 10 vai até 0 passo - 1
    print(num)

gerar lista com range
lista = list(range())
print(lista)

"""