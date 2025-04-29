'''
Faça um program que determine os cinco primeiros múltiplos de 3, considerando números maiores que 0
'''
ns = []
for num in range(1, 16):
   if num % 3 == 0:
       ns.append(num)
print(f'Os 5 primeiros multiplos de 3 são {ns}')
