from time import sleep
"""
faça um programa que some todos os numeros naturais abaixo de 1000 que são multiṕlos de 3 ou 5.
"""

s = 0
for i in range(0, 1000, 3):
    sleep(0.02)
    print(f"Indice/soma {i} : {s}")
    s = s + i
            
print(f"A soma de todos os multiplos de 3 ou 5 até o numero 1_000 é = {s}")