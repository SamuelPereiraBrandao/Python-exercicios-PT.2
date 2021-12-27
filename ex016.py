from math import trunc, floor, ceil
inteiro = float(input("Digite um numero quebrado utilizando o ponto(.)"))
print("O numero = {} arredondando ele para cima ficara:{}".format(inteiro, ceil(inteiro)))
print("O numero = {} arredondando ele para baixo ficara:{}".format(inteiro, floor(inteiro)))
print("O numero = {} e sua porção inteira é: {}".format(inteiro, trunc(inteiro)))
''' 2 opção '''
print(" 2 opção = O numero = {} e sua porção inteira é: {}".format(inteiro, int(inteiro)))
