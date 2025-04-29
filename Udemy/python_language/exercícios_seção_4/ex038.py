# Faça um programa que leia o preço de um produto e o seu desconto e mostre o novo preço

des = float(input('Digite o desconto: '))
pre = float(input('Digite o preço do produto: '))
pcd = pre - (pre * (des / 100))
print(f'O preço com desconto de \033[33m{des}\033[m é de \033[35m{pcd:.2f}\033[m')
