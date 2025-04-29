"""
Saindo de um loop com break
funciona da mesma forma que na linguagem c ou java
utilizamos o break para sair de loop de maneira projetada
"""
# Exemplo 1
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop')

# Exemplo 2
while True:
    comando = input('Digite "sair" para sair: ')
    if comando == 'sair':
        break

