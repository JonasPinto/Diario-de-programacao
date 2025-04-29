"""Um produto vai sofrer aumento de acordo com tabela abaixo. Leia o preço antigo, caucule e escreva o preço novo, escreva uma mensagem em função do preço novo (de acordo com a segunda tabela)
          table 1                                       table 2
Preço antigo           Aumento            Preço novo                Mensagem
até R$ 50                5%               até R$ 80                 barato
entre R$ 50 e R$ 100     10%              entre R$ 80 e R$ 120      normal
acima de R$ 100          15%              entre R$ 120 e R$ 200     caro
                                          acima de R$ 200           muito caro
"""

pr_ant = float(input('Digite o preço atual:  '))

if pr_ant < 50:
    nov_pr = pr_ant + (pr_ant * 0.05)
elif pr_ant >= 50 and pr_ant <= 100:
    nov_pr = pr_ant + (pr_ant * 0.1)  
elif pr_ant > 100:
    nov_pr = pr_ant + (pr_ant * 0.15)

if nov_pr <= 80:
    ms_f = 'Barato'
elif nov_pr > 80 and nov_pr <= 120:
    ms_f = 'Normal'
elif nov_pr > 120 and nov_pr <= 200:
    ms_f = 'Caro'
elif nov_pr > 200:
    ms_f = 'Muito caro'

print(f'O novo preço de R${nov_pr:.2f} é {ms_f} comparado ao preço anterior de R${pr_ant:.2f}')
