

# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 1 - Problem 7
# Description:


"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
Seis valores, negativos e/ou positivos.
Exemplo:
Valor (1/6): 7
Valor (2/6): -5
Valor (3/6): 6
Valor (4/6): -3.4
Valor (5/6): 4.6
Valor (6/6): 12

Processes:
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Output(s):
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
Exemplo:
Detectamos 4 valores positivos.
"""


def main():
    valor1 = int(input(f"Valor (1/6): "))
    valor2 = int(input(f"Valor (2/6): "))
    valor3 = int(input(f"Valor (3/6): "))
    valor4 = int(input(f"Valor (4/6): "))
    valor5 = int(input(f"Valor (5/6): "))
    valor6 = int(input(f"Valor (6/6): "))
    quant = 0
    if valor1 > 0:
      quant = quant +1
    if valor2 > 0:
      quant = quant +1
    if valor3 > 0:
      quant = quant +1
    if valor4 > 0:
      quant = quant +1
    if valor5 > 0:
      quant = quant +1
    if valor6 > 0:
      quant = quant +1
    print(f"Detectamos {quant} valores positivos.")


if __name__ == '__main__':
    main()
