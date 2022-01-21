n1 = float(input("digite a primeira nota"))
n2 = float(input("digite a segunda nota"))
m = (n1 + n2)/2
print("A sua media foi {} pontos".format(m))
if m >= 6.0:
    print("Parabens, você passou de ano!")
else:
    print("Infelizmente você tirou {} pontos, e por isso entrará em recuperação!".format(m))
