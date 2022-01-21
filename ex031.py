velo = float(input("Quantos km está o carro?"))
multa = (velo - 80) * 7
kmamais = (velo - 80)

if velo <= 80.0:
    print("Tenha um bom dia! Dirija com segurança!")
else:
    print("="*89)
    print("Voce está á {}km a mais que o permitido(80km), e por isso levará uma multa de {}R$".format(kmamais, multa))
    print("="*89)
