# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def verifica_fibonacci(numero):
    fib_ant = 0
    fib_atual = 1

    if numero == 0 or numero == 1:
        return True

    while fib_atual <= numero:
        if fib_atual == numero:
            return True
        fib_prox = fib_ant + fib_atual
        fib_ant = fib_atual
        fib_atual = fib_prox

    return False

numero_verificar = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if verifica_fibonacci(numero_verificar):
    print(f"O número {numero_verificar} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_verificar} não pertence à sequência de Fibonacci.")