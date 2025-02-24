"""Programa que dado um conjunto de N números, determina o menor, maior e a soma dos valores"""

valores = []

print("Digite um número de cada vez. Para encerrar, digite '0' para encerrar: \n\n")

while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    else:
        valores.append(numero)


print(f"O menor valor é {min(valores)}\n")

print(f"O maior valor é {max(valores)}\n")

print(f"A soma de todos os números é {sum(valores)}\n")    