# Faça um programa que caucule o ano de uma pessoa a partir do ano atual e de sua data de nascimento

import datetime

# pedir ao usuario para inserir a sua data de nascimento
data_nascimento = input("Digite a sua data de nascimento (dd/mm/yyyy)\n>>> ")
data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y").date()
print("Você nasceu em "+ data_nascimento.strftime("%d") + " de " + data_nascimento.strftime("%B, %Y"))

data_atual = datetime.datetime.today().date()

idade = data_atual.year - data_nascimento.year
monthVeri = data_atual.month - data_nascimento.month
dateVeri = data_atual.day - data_nascimento.day

#Type conversion here
idade = int(idade)
monthVeri = int(monthVeri)
dateVeri = int(dateVeri)

if monthVeri < 0:
    idade = idade - 1
elif dateVeri < 0 and monthVeri == 0:
    idade = idade - 1


#lets print the age now
print(f'Você tem {idade} anos de idade')
