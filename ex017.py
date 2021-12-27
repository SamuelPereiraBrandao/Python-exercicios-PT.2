from math import hypot
catop = float(input("comprimento do cateto oposto:"))
catadj = float(input("comprimento do cateto adjacente:"))
hi = (catop ** 2 + catadj ** 2) ** (1 / 2)
print("A hipotenusa vai medir {:.2f}".format(hi))

''' 2 OPÇÃO '''

co = float(input("comprimento do cateto oposto:"))
ca = float(input("comprimento do cateto adjacente:"))
hi2 = hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hi2))
