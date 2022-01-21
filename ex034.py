n1 = int(input("Digite um numero"))
n2 = int(input("Digite outro numero"))
n3 = int(input("Digite outro o ultimo numero"))

# verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print("O menor valor foi {} e o maior valor foi {}".format(menor, maior))
