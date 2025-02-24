"""Programa determina se um número é primo ou não"""

numero = int(input("Digite um número inteiro:"))
primo = True

if numero <= 1:
    print("O número não é primo")
    exit()

for i in range(2, numero):
    
    if numero % i == 0:
        primo = False
if primo:
    print("O número é primo")
else:
    print("O número não é primo.")
       