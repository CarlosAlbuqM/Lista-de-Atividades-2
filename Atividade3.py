"""Calculadora de adição"""

while True:

    print("Operação - Adição \n")
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))

    resultado = numero1 + numero2

    print(f"{numero1} + {numero2} = {resultado}\n\n")

    escolha = str(input("Deseja realizar mais uma soma? [S ou N]: \n")).upper()
    if escolha == 'S':
        continue
    elif escolha == 'N':
        print("Até logo")
        break


