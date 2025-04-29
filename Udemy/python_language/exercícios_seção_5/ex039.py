'''
Uma empresa decide dar um almento aos seus funcionários de acordo com uma tabela que considera o salário atual  e o tempo de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente maior do que os funcionários com salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus adicional de salário. Faça um programa que leia:
 - o valor do salário atual do funcionário.
 - o tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).
Use a tabela abaixo para caucular o salário reajustado deste funcionário e imprima o valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.

  Salário Atual   /   Reajuste   /   Tempo de serviço   /   Bônus
  Até 500,00            25%            Abaixo de 1 ano     Sem bônus
  Até 1000,00           20%            De 1 a 3 anos        100,00
  Até 1500,00           15%            De 4 a 6 anos        200,00
  Até 2000,00           10%            De 7 a 10 anos       300,00
  Acima de 2000,00   Sem reajuste      Mais de 10 anos      500,00
'''
from sys import exit

sal_atual = int(input('Digite o valor do salário atual : '))
tim_work = int(input('Digite o tempo de serviço em anos\ncaso não tenha um ano completo digite zero : '))
reajuste = 0
bonus = 0
sal_atuali = 0

if sal_atual > 0 and sal_atual <= 500 :
    sal_atuali = sal_atual + (sal_atual * 0.25)
    reajuste = 25

if sal_atual > 500 and sal_atual <= 1000 :
    sal_atuali = sal_atual + (sal_atual * 0.20) 
    reajuste = 20

if sal_atual > 1000 and sal_atual <= 1500 :
    sal_atuali = sal_atual + (sal_atual * 0.15)
    reajuste = 15

if sal_atual > 1500 and sal_atual <= 2000 :
    sal_atuali = sal_atual + (sal_atual * 0.10)
    reajuste = 10

if tim_work > 0 and tim_work <= 3:
    bonus = bonus + 100

if tim_work > 3 and tim_work <= 6:
    bonus = bonus + 200

if tim_work > 6 and tim_work <= 10:
    bonus = bonus + 300

if tim_work > 10:
    bonus = bonus + 500

if sal_atual > 2000 or tim_work < 1:
   if sal_atual > 2000 and tim_work < 1:
      print(f'O salário de R$ {sal_atual} não terá direito á reajuste e também não terá direito a bônus por tempo de trabalho Totalizando R$ {sal_atual}')
      exit()

   if sal_atual > 2000:
      print(f'O salário de R$ {sal_atual} não tem direito á reajuste mas receberá R$ {bonus} de bônus por tempo de trabalho Totalizando R$ {sal_atual + bonus}')
      exit()

   if tim_work < 1:
      print(f'O salário de R$ {sal_atual} receberá {reajuste} % de reajuste + mas não terá direito á bônus por tempo de trabalho Totalizando R$ {sal_atuali}')
      exit()
   
print(f'O salário de R$ {sal_atual} receberá {reajuste} % de reajuste + R$ {bonus} de bônus por tempo de trabalho Totalizando R$ {sal_atuali + bonus}')


