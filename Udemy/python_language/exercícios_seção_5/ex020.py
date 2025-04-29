"""
Dados tres valores A,B,C verificar se eles podem formar um triangulo a partir da regra (o comprimento de cada
 lado do triangulo deve ser menor que a soma dos outros dois lados) e determinar que tipo de triangulo podem formar:
 Equilatero  -> tres lados iguais
 Escaleno    -> dois lados iguais
 Isosceles   -> todos os lados diferentes
"""
import sys
l1 = float(input('Digite o 1° lado do triangulo: '))
l2 = float(input('Digite o 2° lado do triangulo: '))
l3 = float(input('Digite o 3° lado do triangulo: '))

if (l3 > (l1 + l2)) or (l2 > (l1 + l3)) or (l1 > (l2 + l3)):
    print('Com essas medidas não se pode formar um triangulo')
    sys.exit()
elif l1 == l2 and l1 == l3 and l2 == l3:
    print('Esse triangulo é EQUILÁTERO')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Esse triangulo é ISÓSCELES')
elif l1 != l2 and l1 != l3 and l2 != l3:
    print('Esse trinagulo é ESCALENO')

