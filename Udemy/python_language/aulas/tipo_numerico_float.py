"""
Tipo float ou real com casas decimais

Obs: O separador de casas decimais é o ponto (.) e não virgula (,)

"""
# Errado
valor = 1, 4   # a virgula gera uma tupla ou lista de dois números
print(valor)
print(type(valor))

# Certo
valor = 1.4
print(valor)
print(type(valor))

# É possivel fazer dupla atribuição
valor1, valor2 = 1, 4  # nesse caso cada variavel recebe um valor inteiro
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# podemos converter um float para int, mas perde-se precisão
res = int(valor)
print(res)
print(type(res))


