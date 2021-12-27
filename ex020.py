from random import shuffle

aluno1 = str("João")
aluno2 = str("Samuel")
aluno3 = str("Aline")
aluno4 = str("Beatriz")
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print("A ordem de quem da apresentação será essa: {}".format(lista))
