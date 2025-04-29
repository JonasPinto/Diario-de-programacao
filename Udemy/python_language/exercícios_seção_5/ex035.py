"""
Leia uma data e determine se ela é valida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe naquele mês. Note que fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos 
"""
import sys
mes_str = {1: '31Janeiro', 2: '', 3: '31Março', 4: '30Abril', 5: '31Maio', 6: '30Junho', 7: '31Julho', 8: '31Agosto', 9: '30Setembro', 10: '31Outubro', 11: '30Novembro', 12: '31Dezembro'}

data = str(input('digite a data no formato DD/MM/YYYY\n'))
if len(data) == 10:
    dia = data[:2]
    mes = int(data[3:5])
    ano = int(data[6:10])
else:
    print('\nFormato de data incorreto')
    sys.exit
if (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0)):
    inf_biss = 'é bissexto'
    mes_str[2] = '29Fevereiro'
else:
    inf_biss = 'não é bissexto'
    mes_str[2] = '28Fevereiro'

if (mes >= 1 and mes <= 12) and int(dia) > 0:
    for i in mes_str:
        mes_out = mes_str[mes]
        dia_out = mes_out[0:2] 
        if dia <= dia_out:
            valido = 'válida'
        else:
            valido = 'inválida'
else: 
    print('O mês digitado é inválido')
    sys.exit
print(f'A data {data} é {valido}, o ano {ano} {inf_biss} e o mês de {mes_out[2:]} tem {mes_out[0:2]} dias')


   
