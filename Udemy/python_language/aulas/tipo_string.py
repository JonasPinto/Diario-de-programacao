"""
Tipo string

Em python um dado é considerado do tipo string sempre que:
-Estiver entre aspas simples          -> 'oi tudo bem', '123', 'a', 'True', '43.45'
-Estiver entre aspas duplas           -> "oi tudo bem", "123", "a", "True", "43.45"
-Estiver entre aspas simples triplas -> '''oi tudo bem''', '''123''', '''a''', '''True''', '''43.45'''

nome = 'jonas pinto'
print(nome)
print(type(nome))

nome = "jona 's pinto"  # usar aspas duplas caso a palavra use apostrophe   Exemplo: (let`go)
print(nome)
print(type(nome))

nome = "jonas \" pinto"  # a contrabarra pode ser usada como caractere de escape
print(nome)              # onde possibilita o uso da mesma aspas dentro da string
print(type(nome))

nome = 'jonas da silva pinto'
print(nome.upper())  # transforma a string de minusculo para maiusculo
print(nome.lower())  # transforma de maiusculo para minusculo
print(nome.split())  # transforma a frase ou texto em uma lista
# [   0,     1,      2,       3   ]  posições para acessar
# ['jonas', 'da', 'silva', 'pinto']
print(nome.split()[3])  # acessa a lista na posição 3

# slice de string
#   0   1   2   3   4   5   6   7   8  9   10  11  12  13  14  15  16  17  18  19
# ['j','o','n','a','s',' ','d','a',' ',s','i','l','v','a',' ','p','i','n','t','o']
print(nome[:4])  # Faz acesso da posição 0 ate a 3
print(nome[15])   # Faz acesso apenas a posição passada
print(nome[6:])   # Faz acesso da posição indicada até a ultima

"""
#-Estiver entre aspas duplas triplas -> """oi tudo bem""", """123""", """a""", """True""", """43.45"""

nome = """jonas da 
silva 
pinto """   # usar aspas duplas triplas ou (\n) pula uma linha
print(nome)
print(type(nome))

print(nome[::-1])
print(nome.replace('j', 'o'))  # troca o caractere indicado por outro indicado também

texto = 'socorram me subino onibus em marrocos'  # Palindromo
print(texto[::-1])  # -> inverte a string











