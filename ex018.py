from math import sin, tan, cos, radians

angul = float(input("Digite o ângulo que você deseja:"))

seno = sin(radians(angul))
print("O ângulo {} tem o seno de {:.2f}".format(angul, seno))

cosseno = cos(radians(angul))
print("O ângulo de {} tem o cosseno de {:.2f}".format(angul, cosseno))

tangente = tan(radians(angul))
print("O ângulo {} tem a tangente de {:.2f}".format(angul, tangente))
