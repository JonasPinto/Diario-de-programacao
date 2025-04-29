"""
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar
condições para aposentadoria
- ter 65 anos ou mais
- ou ter trabalhado no minimo 30 anos
- ou ter pelo menos 60 anos e ter trabalhado 25 anos
"""
print('***************************************************************')
print('                  CALCULADORA DE APOSENTADORIA')
print('***************************************************************')
id = int(input('Digite a idade            ->    '))
ts = int(input('Digite o tempo de serviço ->    '))
if (id >= 65) or (id >= 44 and ts >= 30) or (id >= 60 and ts >= 25):
    print('\nAposentadoria \033[34mCONSEDIDA\033[m')
else:
    print('Aposentadoria \033[32mNEGADA\033[m')