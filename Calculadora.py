#APRENDER A USAR LISTAS NO CÓDIGO.

print ("------------------------------------")
print ("Calculadora Simples")
print ("------------------------------------")

while True:
    quantidade = int(input("Quantos números deseja inserir para calcular? "))
    numeros = []
    for i in range(quantidade):
        numero = float(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)

    print ("------------------------------------")
    print ("Menu de Operações:\n")
    print ("1 - Adição")
    print ("2 - Subtração")
    print ("3 - Multiplicação")
    print ("4 - Divisão")
    print ("5 - Média")
    print ("6 - Equação de 2º grau")
    print ("7 - Fatorial")
    print ("8 - Conversão de unidades")
    print ("9 - Tabuada")
    print ("10 - Fibonacci")
    print ("11 - Sair")
    print ("------------------------------------")
    escolha = int(input("Escolha a operação desejada: "))
    print ("------------------------------------")

    if escolha == 1:
        resultado = sum(numeros)
        print ("O resultado da adição é:", resultado)
    
    elif escolha == 2:
        resultado = numeros[0]
        for n in numeros[1:]:
            resultado -= n
        print (f"O resultado da subtração é: {resultado:.2f}")
    
    elif escolha == 3:
        resultado = 1
        for n in numeros:
            resultado *= n
        print ("O resultado da multiplicação é:", resultado)
    
    elif escolha == 4:
        if any(n == 0 for n in numeros[1:]):
            print ("Erro: Não pode dividir por zero. Tente novamente.")
        else:
            resultado = numeros[0]
            for n in numeros[1:]:
                resultado /= n
            print (f"O resultado da divisão é: {resultado:.2f}")
    
    elif escolha == 5:
        resultado = sum(numeros) / quantidade
        print (f"O resultado da média é: {resultado:.2f}")

    elif escolha == 9:
        numero = numeros[0]
        print (f"A tabuada do {numero} é:\n")
        for i in range(11):
            resultado = numero * i
            print (f"{numero} x {i} = {resultado}")

    elif escolha == 11:
        print ("Encerrando a calculadora. Até mais!")
        break

    else:
        print ("Opção inválida. Tente novamente!")

    print ()