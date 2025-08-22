"""
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequência arbitrária de notas (válidas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente média aritimética. O número de notas com que o aluno pretende efetuar o cauculo não será fornecido ao programa, o qual terminará quando for introduzido um valor que não seja válido como nota de aprovação.  
"""

notas = []
print("Digite as notas (entre 10 e 20). Para encerrar, digite um valor fora desse intervalo.")

while True:
    try:
        nota = float(input("Digite uma nota: "))
        if 10 <= nota <= 20:
            notas.append(nota)
        else:
            print("Valor inválido detectado. Encerrando entrada de dados...")
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia aritmética das notas válidas: {media:.2f}")
else:
    print("\nNenhuma nota válida foi informada.")
