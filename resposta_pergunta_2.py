"""
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

Resposta abaixo no código em Python:
"""


def letra_a_existe(string):
    string_lower = string.lower()

    contagem = string_lower.count("a")

    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vezes.")
    else:
        print("A letra 'a' não aparece na string.")


string = input("Digite uma string: ")

letra_a_existe(string)
