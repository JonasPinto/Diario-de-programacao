"""
Estruturas Lógicas and(e), or(ou), not(não), is(é)
operadores unários:
 - not
operadores binarios:
 - and, or

 Regras de funcionamento
 Para o and, ambos os valores precisam ser True(verdadeiro)
 Para o or, um ou outro valor precisa ser True
 Para o not, o valor logico é invertido
 Para o is, o valor é comparado exemplo (1 == 2 ?)  (1 is 2 ?)
"""
ativo = True
logado = True

if ativo or logado:
    print('Bem vindo usuario')
else:
    print('Você precisa ativar sua conta')

