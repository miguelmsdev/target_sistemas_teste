"""
3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?

Resposta:
O valor da variável SOMA é 11

Abaixo o código fonte na linguagem Python.
"""

INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K += 1
    SOMA += 1
    print(SOMA)
