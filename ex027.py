nome = str(input("Digite seu nome completo:")).strip()
nome = nome.split()
print("Primeiro nome: {}".format(nome[0]))
print("Seu último nome: {}".format(nome[len(nome) - 1]))
# 2 opção
nome1 = input('Qual o seu nome completo? ')
m = nome1.split()
print(f'Seu primeiro nome é {m[0]} e seu último nome é {m[-1]}')
