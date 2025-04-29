"""
https://docs.python.org/3/library/collections.html?highlight=collections#collections.Counter

Módulo collections - Counter (contador)

Collections -> High-performance Datetypes

counter -> Recebe um iteravel como parametro e cria um objeto do tipo Collections Counter que é paracido com um dicionário, contendo como chave o elemento da lista passada como parametro e como valor a quantidade de ocorrência desse elemento

# Exemplo 1
# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o counter
res = Counter(lista)
print(type(res))
print(res)
# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})
# Veja que para cada elemento da lista, o counter criou um chave e colocou como valor a quantidade de ocorrências

# Exemplo 2
print(Counter('Jonas da silva pinto'))
# Counter({'a': 3, ' ': 3, 'o': 2, 'n': 2, 's': 2, 'i': 2, 'J': 1, 'd': 1, 'l': 1, 'v': 1, 'p': 1, 't': 1})
"""

from collections import Counter

texto = """  Buraco negro é uma região do espaço-tempo em que o campo gravitacional é tão intenso que nada — nenhuma partícula ou radiação eletromagnética como a luz — pode escapar dela. A teoria da relatividade geral prevê que uma massa suficientemente compacta pode deformar o espaço-tempo para formar um buraco negro. O limite da região da qual não é possível escapar é chamado de horizonte de eventos. Embora o horizonte de eventos tenha um efeito enorme sobre o destino e as circunstâncias de um objeto que o atravessa, não tem nenhuma característica local detectável. De muitas maneiras, um buraco negro age como um corpo negro ideal, pois não reflete luz. Além disso, a teoria quântica de campos no espaço-tempo curvo prevê que os horizontes de eventos emitem radiação Hawking, com o mesmo espectro que um corpo negro de temperatura inversamente proporcional à sua massa. Essa temperatura é da ordem dos bilionésimos de um kelvin para buracos negros de massa estelar, o que a torna praticamente impossível de observar.
"""
palavras = texto.split() # Separa cada palavra do texto
print(palavras)

res = Counter(palavras) # Separa cada palavra e mostra quantas vezes ela aparece
print(res)
print(res.most_common(5)) # Mostra as 5 palavras que mais ocorrem no texto


# para acessar a documentação complata da linguagem python acessar -> https://www.python.org/