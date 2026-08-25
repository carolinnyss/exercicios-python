#Usar o import math

a = float(input("Digite o valor do coeficiente 'a': "))
b = float(input("Digite o valor do coeficiente 'b': "))
c = float(input("Digite o valor do coeficiente 'c': "))


delta = b**2 - 4*a*c

x1 = (-b + (delta**1/2))/ (2*a)
x2 = (-b - (delta**1/2)) / (2*a)

print ("O valor da primeira raiz é: %.2f " % (x1))
print ("O valor da segunda raiz é: %.2f " % (x2))