from random import randint
from time import sleep

computador = randint(0, 5)  # faz o computador "pensar"
print("-=-" * 20)
print("Vou pensar em um número de 0 á 5, tente adivinhar!")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei?"))  # jogador tenta adivinhar!
print("Processando...")
sleep(2)
if jogador == computador:
    print("Parabéns! Você conseguiu me vencer!")
else:
    print("PERDEU! Eu pensei no número {} e não no {}!".format(computador, jogador))
