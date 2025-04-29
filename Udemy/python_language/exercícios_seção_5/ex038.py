"""
Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: Dia, Mês e Ano. Teste a validade desta data para saber se esta data é uma data válida. Teste se o dia fornecido é válido: dia > 0, dia < = 28 para o mes de fevereiro (29 se o ano for bissexto), dia < = 30 em abril,junho, setembro e novembro, dia < = 31 nos outros meses. Teste a validade do ano: ano < = ano atual, imprimir data valida ou invalida ao final da execução do programa.

"""
print('DD/MM/YYYY')
Data = input('Digite a data de nascimento ')
dia = int(Data[:2])
mes = int(Data[3:5])
ano = int(Data[6:])
res = 'invalida'

if (dia > 0 and dia <= 31) and (mes > 0 and mes < 13) and (ano > 0 and ano <= 2020):
    if mes == 2:
        if (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0)):
            if dia <= 29:
                res = 'valida'
        if dia <= 28:
            res = 'valida'    
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia <= 31:
            res = 'valida'
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
         if dia <= 30:
            res = 'valida'
else:
    res = res 

print(f'A Data digitada é {res}')