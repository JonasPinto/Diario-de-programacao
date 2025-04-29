""" Mapas -> Conhecidos em python como dicionarios Dicionarios em python são representados por chaves {} 

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# iterar sobre dicionarios
for chave in receirta:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

# Acessando as chaves
print(receita.keys())
for chave in receita.keys():
    print(receita[chave])

# Acessando valores 
print(receita.values())
for valor in receita.values():
    print(valor)

# Desenpacontamento de dicionarios
print(receita.items())
for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

# Soma*, valor maximo*, valor minimo*, tamanho* se os valores forem todos inteiros ou reais
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}

