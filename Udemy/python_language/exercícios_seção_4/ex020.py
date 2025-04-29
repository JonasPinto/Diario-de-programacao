# Leia um valor de massa em quilogramas e apresente-o convertido em libras. L = K / 0.45

k = float(input('Digite o peso em kg: '))
l = k / 0.45
print(f'\033[35m{k}\033[m Kg equivalem a \033[35m{l:.2f}\033[m Libras')


