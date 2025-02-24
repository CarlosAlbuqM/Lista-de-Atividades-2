"""Programa que dado um conjunto de N números, determina o menor, maior e a soma dos valores, porém aceitando apeenas números entre 0 e 1000"""
valores = []

print("Digite um número de cada vez. Para encerrar, digite enter para encerrar: \n\n")

while True:
    try:
        numero = int(input("Digite um número: "))
        if numero < 0 or numero > 1000:
            print("Digite apenas números entre 0 e 1000")
            continue
        elif numero >= 0 and numero <= 1000:
            valores.append(numero)
    except ValueError:
        print("Até logo \n\n")
        break
 

print(f"{valores}\n")

print(f"O menor valor é {min(valores)}\n")

print(f"O maior valor é {max(valores)}\n")

print(f"A soma de todos os números é {sum(valores)}\n")    
