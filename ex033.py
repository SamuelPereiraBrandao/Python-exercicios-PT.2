viagem = float(input("Quantos km irá ter sua viagem?"))
if viagem <= 200:
    valor = viagem * 0.50
    print("O Valor da sua viagem será de: {}R$".format(valor))
else:
    valor2 = viagem * 0.45
    print("O valor da sua viagem será de: {}R$".format(valor2))
