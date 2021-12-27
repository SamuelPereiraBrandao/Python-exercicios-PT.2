from random import choice
n1 = str("JOÁO")
n2 = str("MARIA")
n3 = str("THOMAS")
n4 = str("ALINE")
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print("O aluno escolhido foi o: {}".format(escolhido))
