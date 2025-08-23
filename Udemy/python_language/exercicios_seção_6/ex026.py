"""
Faça um algoritmo que encontre o primeiro multiplo de 11, 13 ou 17 após um número dado
""" 

def proximo_multiplo(n):
    while True:
        n += 1
        if n % 11 == 0:
             return n, 11
        elif n % 13 == 0:
            return n, 13 
        elif n % 17 == 0:
            return n, 17

numero = int(input("Digite um número: "))
resultado, multiplo = proximo_multiplo(numero)
print(f"O primeiro múltiplo de 11, 13 ou 17 após o numero {numero} = {resultado}\nO numero {resultado} é multiplo de {multiplo}\n{resultado}/{multiplo} = {resultado/multiplo}")

