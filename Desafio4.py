"""Programa que lê e valida algumas informações: (nome)(idade)(salário)(sexo)(estado civil)"""

while True:
    nome = str(input("Digite seu nome: "))
    if len(nome) <= 3:
        print("O nome deve contar mais de 3 caracteres")
    else:
        break

while True:
    idade = int(input("Digite sua idade: "))
    if idade < 0 or idade > 150:
        print("Digite uma idade válida")
    else:
        break

while True:
    salario = float(input("Digite seu salário R$"))
    if salario <= 0:
        print("Você precisa de um salário para continuar")
    else:
        break

while True:
    sexo = str(input("Qual seu sexo 'M' OR 'F'? ")).upper()
    if sexo != 'M' and sexo != 'F':
        print("Digite um gênero válido.")
    else:
        break

while True:
    estado_civil = str(input("Digite seu estado civil 'S','C','V','D': ")).upper()
    if estado_civil not in ['S','C','V','D']:
        print("Digite um estado civil válido.")
    else: 
        break

print(f"Seu nome é {nome} do sexo {sexo} e você tem {idade} anos. O seu salário é de R${salario}. Atualmente seu estado civil é {estado_civil}." ) 