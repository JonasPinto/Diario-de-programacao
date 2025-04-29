"""
As tarifas de certo parque de estacionamento são as seguintes:

1ª e 2ª hora - R$ 1,00 cada
3ª e 4ª hora - R$ 1,40 cada
5ª e seguintes - R$ 2,00 cada

O número de horas a pagar é sempre inteiro arredondado por excesso. Deste modo, quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria se tivesse permanecido 120 minnutos. Crie um programa que, lidos pelo teclado os momentos de chegada e partida, escreva na tela o preço cobrado pelo estacionamento.
"""

print('-----------------------------------------')
print('             PARQUIMETRO                 ')
print('-----------------------------------------')
print('Formato de data dd/mm')
print('Formato de hora 24h 00:00')

dt_chegada = input('Data de entrada -> ')
hr_chegada = input('Hora de entrada -> ')
dt_saida = input('Data de saída -> ')
hr_saida = input('Hora de saída -> ')

if hr_saida == '00:00':
    hr_saida = '24:00'
    
if dt_saida == dt_chegada:
    mn_tot_c = int(hr_chegada[:2]) * 60 + int(hr_chegada[3:])
    mn_tot_s = int(hr_saida[:2]) * 60 + int(hr_saida[3:]) 
    tot_t = mn_tot_s - mn_tot_c
else:
    mn_tot_c = 1440 - (int(hr_chegada[:2]) * 60 + int(hr_chegada[3:]))
    dias_estacionado = (int(dt_saida[:2]) - int(dt_chegada[:2])) - 1
    mn_tot_s = int(hr_saida[:2]) * 60 + int(hr_saida[3:]) 
    tot_t = dias_estacionado * 1440 + mn_tot_c + mn_tot_s  

if tot_t <= 60:
    tot_pg = 1
elif tot_t > 60 and tot_t <= 120:
    tot_pg = 2
elif tot_t > 120 and tot_t <= 180:
    tot_pg = 4.20
elif tot_t > 180 and tot_t <= 240: 
    tot_pg = 5.6
else:
    if tot_t % 60 == 0:
        tot_pg = (tot_t // 60) * 2 
    else:
        tot_pg = (tot_t // 60) * 2  + 2

print(f'O total a pagar é R${tot_pg:.2f}')

