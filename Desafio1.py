"""Programa do Fibonacci"""

def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq_fib = fibonacci(n - 1)
        seq_fib.append(seq_fib[-1] + seq_fib[-2])
        return seq_fib
    
try:

        num = int(input("Digite a quantidade de fibbonaccis a gerar: "))
        res = fibonacci(num)
        print(f'Sequência de fibonnaci gerado é: {res}')
except RecursionError:
        print(f'Deve ser fornecido um número inteiro positivo válido.')