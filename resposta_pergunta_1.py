"""
Técnica:

1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

Resposta abaixo no código em Python:
"""


def pertence_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n


numero = int(input("Informe um número: "))

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência.")
else:
    print(f"O número {numero} NÃO pertence à sequência.")
