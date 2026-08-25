n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))


print("-------------------------------")
print("Menu de operações")
print("-------------------------------\n")

print("1 - Soma")
print("2 - Subtração\n")

escolha = int(input("Escolha uma operação a ser realizada: "))

soma = n1 + n2
sub = n1 - n2

if escolha == 1:
   print ("A soma entre", n1,"e", n2,"é igual a", soma)
else:
    print ("A subtração entre", n1,"e", n2,"é igual a", sub)

