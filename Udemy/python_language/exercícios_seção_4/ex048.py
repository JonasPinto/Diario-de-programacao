# Leia um valor inteiro em segundos e imprima-o em horas minutos e segundos

print('\033[33m*********************************\033[m')
print('     \033[35mCONVERSOR DE HORAS\033[m')
print("\033[33m*********************************\033[m")
print('\033[36m[1]\033[m Segundos p/ Horas Minutos Segundos')
print('\033[34m[2]\033[m Horas Minutos Segundos p/ Segundos')
op = int(input('Digite a opção -> '))

if op == 1:
   seg = int(input('Digite os segundos: '))
   h = seg // 3600
   sgr = seg % 3600
   m = sgr // 60
   s = sgr % 60
   print(f'\033[36m{seg}\033[m segundos correspondem a \033[32m{int(h)} Horas {int(m)} Minutos {int(s)} Segundos\033[m')
elif op == 2:
    h = int(input('Horas: '))
    m = int(input('Minutos: '))
    s = int(input('Segundos: '))
    tots = (h * 3600) + (m * 60) + s
    print(f'\033[31m{h}:{m}:{s}\033[m São equivalente a \033[31m{tots}\033[m Segundos')
else:
    print('\033[31mOPÇÃO INVALIDA\033[m')