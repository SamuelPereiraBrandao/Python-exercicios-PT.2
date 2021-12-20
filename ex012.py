preco = float(input("qual e o preco do produto? *desconto de 15%* | R$"))
novo = preco - (preco * 15 / 100)
print("o produto que custava {} R$, na promocao com desconto de 15% vai custar {} R$".format(preco, novo))
