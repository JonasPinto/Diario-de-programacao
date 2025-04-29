"""
 Leia o salário de um trabalhador e o valor da prestação de um emprestimo. se a prestação for maior qua 20% do salário
imprima: Emprestimo não consedido, caso contrario imprima: Emprestimo concedido.
"""
sal = float(input('Digite o valor do salário: '))
v_imp = float(input('Digite o valor da parcela do seu emprestimo: '))
res = (v_imp * 100) / 1500
if res > 20:
    print('Emprestimo não consedido')
else:
    print('Emprestimo conedido')
