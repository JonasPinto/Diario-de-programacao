"""
Faça um programa para ler as dimenções de um terreno (comprimento e largura) e o preço do metro da tela
imprima a metragem linear de tela necessria para cercar esse terreno bem como o custo da tela.
"""
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
p = float(input('Qual o preço da tela por metro R$: '))

mli = (l * 2) + (c * 2)
cus = mli * p

print(f'Para cercar todo o terreno é necessario {mli:.2f} Metros lineares de tela\n'
      f'O custo fica em R${cus:.2f} Reais para cercar todo o terreno')
