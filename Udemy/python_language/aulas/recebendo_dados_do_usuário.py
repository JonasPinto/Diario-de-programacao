"""
       Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo string

Em python, string é tudo oque estiver entre
- Aspas simples -> ''
-Aspas duplas -> ""
-Aspas simples triplas -> ''' '''
-Aspas duplas triplas -> """ """

"""

# input() -> entrada de dados
nome = input("Qual é o seu nome? ")

# exemplo de print antigo versao 2.x
print('Seja ben vinda %s' % nome)

# Exemplo de print moderno versão 3.x
print('Seja bem vinda {0}'.format(nome))

# Exemplo de print mais atual versão 3.8
print(f'seja bem vinda {nome}')


print('Qual a sua idade? ')
idade = input()

# Processamento

# Exemplo print 2.x
print('A %s tem %s anos' % (nome, idade))

# Exemplo de print 3.x
print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 3.8
print(f'A {nome} tem {idade} anos')

# Exemplo print com cauculo
print(f'A {nome} nasceu em {2020 - int(idade)}')