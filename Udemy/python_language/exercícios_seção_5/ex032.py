""" Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade, o programa deve calcular o valor a ser pago por aquele pedido, o cardapio da lanchonete segue o seguinte padrão

Especificação        Código    Preço 

Cachorro quente        100      1.20
Bauru simples          101      1.30
Bauru com ovo          102      1.50
Hamburguer             103      1.20
Cheeseburguer          104      1.70
Suco                   105      2.20
Refrigerante           106      1.00
"""

cardapio = [{'nome': 'cachorro quente', 'codigo': 100, 'preço': 1.20},
            {'nome': 'bauru simples',   'codigo': 101, 'preço': 1.30},
            {'nome': 'bauru com ovo',   'codigo': 102, 'preço': 1.50},
            {'nome': 'hamburguer',      'codigo': 103, 'preço': 1.20},
            {'nome': 'cheeseburguer',   'codigo': 104, 'preço': 1.70},
            {'nome': 'suco',            'codigo': 105, 'preço': 2.20},
            {'nome': 'refrigerante',    'codigo': 106, 'preço': 1.00}]

op = ''
pg = 0

while op != 's':
    cod = int(input('CODIGO DO PEDIDO  '))
    qtd = int(input('QUANTIDADE  '))
    for iten in cardapio:
        if iten['codigo'] == cod:
            pg += iten['preço'] * qtd  
    op = input('[ S ] Sair [ ENTER ] Continuar ')           
print(f'Total = R$ {pg:.2f}')
