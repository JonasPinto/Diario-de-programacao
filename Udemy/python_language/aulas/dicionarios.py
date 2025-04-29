"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionarios (python) são conhecidos por mapas.
Dicionários são coleções do tipo chave/ valor
Dicionarios são representados por {} chaves
print (type({}))
OBS: sobre dicionarios
    - chave e valor são representados por dois pontos -> 'chave': 'valor'
    - tanto chave quanto valor podem ser de qualquer tipo de dado
    - podemos misturar tipos de dados

# criação de dicionarios
# forma 1 (Mais comun)
paises = {'br': 'Brasil', 'eua': 'Estados unidos', 'py': 'Paraguay'}

print(paises)
print(type(paises))

#forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados unidos', py='Paraguay')

print(paises)
print(type(paises))

# acessando elementos
# forma 1 - Acessando via chave,  da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])

# OBS: Caso tentemos fazer acesso utilizando uma chave que não exista, teremos o erro KeyError

# forma 2 - Acessando via get -> recomendada

print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não sera gerado erro
pais = paises.get('ru')


if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrão para caso não encentremos o objeto com a chave informada
pais = paises.get('ru', 'Não encontrado')
print(f'{pais}')

paises = {'br': 'Brasil', 'eua': 'Estados unidos', 'py': 'Paraguay'}

# Podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

# Podemos adicionar uma chave e um novo valor
if 'ru' not in paises:
    paises['ru'] = 'russia'
print(paises)
print(type(paises))

# Podemos utilizar qualquer tipo de dado int, float, string, boolean etc...

# Tuplas são interressantes de serem utilizadas como chave de dicionarios, pois as mesmas são imutáveis

localidades = {
    (35.9874, 33.4635): 'Escritório em marrocos',
    (87.2435, 65.1322): 'Escritório em portugal',
    (51.9984, 76.9387): 'Escritório em cuba',
}
print(localidades)
print(type(localidades))

# Adicionar um elemento em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300 }

# Forma 1
receita['abr'] = 350
print(receita)

# Forma 2 -> usando update para inserir e atualizar chaves e valores
nova_receita = {'mai': 145}
receita.update({'mai': 145}) # usa-se update + chave e valor
receita.update(nova_receita) # usa-se update + variavel criada
print(receita)

OBS: Em dicionarios não se pode ter chaves repetidas

# Remover dados de um dicionario
# Forma 1 - mais comun
receita = {'jan': 100, 'fev': 120, 'mar': 300}
receita.pop('mar')
print(receita)
# OBS: Obrigatorio informar a chave a ser removida

# Forma 2
del receita['fev']
print(receita)
# Se a chave não existir será gerado um keyError
******************************************************************************************************************
# imagine um programa que recebe produtos em um carrinho
carrinho de compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;

# 1 - Poderiamos utilizar uma lista para isso? -> sim

carrinho = []
produto1 = ['playstation', 1, 2300.00]
produto2 = ['good of war', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto.

# 2 - Poderiamos utilizar tupla para isso? sim

produto1 = ('playstation 4', 1, 2300.00)
produto2 = ('good of war', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)

# teriamos que saber qual é o indice de cada informação no produto

# 3 - Poderiamos utilizar um dicionario para isso? sim
carrinho = []

produto1 = {'nome': 'playstation 4', 'qtd': 1, 'R$': 2300.00}
produto2 = {'nome': 'good of war 4', 'qtd': 1, 'R$': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

Desta forma, facilmente adicionamos ou removemos produtos no carrinho  e em cada produto
 podemos ter a certeza sobre cada informação

# Limpar o dicionario (zerar dados)
d.clear()
print(d)
**********************************************************************************************************************
# metodos de dicionarios

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Copiando dicionario para outro

# forma 1 -> deep copy
novo = d.copy()
print(novo)

novo['d'] = 4  # Aqui foi criado + um indice (d) e atribuiu-se a ele o valor 4

print(d)
print(novo)

# Forma 2 -> shellow copy
novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O metodo fromkeys recebe dois parâmetros: um interável e um valor
# Ele vai gerar para cada valor do iteravel uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)
"""
