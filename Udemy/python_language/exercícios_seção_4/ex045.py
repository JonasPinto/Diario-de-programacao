# Faça um programa para converter uma letra maiuscula em minuscula. use a tabela ascii para resolver o problema
l = input('Digite uma letra maiuscula: ')
print(f'A letra **\033[31m{l}\033[m** em maiusculo corresponde ao codigo \033[36m{ord(l)}\033[m na tabela ascci')
min = ord(l) + 32
print(f'Em minusculo **\033[31m{chr(min)}\033[m** corresponde ao codigo \033[36m{ord(l) + 32}\033[m na tabela ascii')


