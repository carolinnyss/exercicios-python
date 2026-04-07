# Inicialmente, o programa solicita ao usuário seu peso e altura.

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

# Em seguida, o programa calcula o Índice de Massa Corporal (IMC),
# usando a fórmula e apresenta o resultado com duas casas decimais.

IMC =  peso / (altura ** 2)
print (f"Seu IMC é: {IMC:.2f}")

# Por fim, o programa calcula com base na tabela da OMS (Organização Mundial da Saúde) 
# e classifica o resultado com base nos status.

if (IMC <= 18.5):
   
    print ("Status: Magreza")
elif (IMC >= 18.6) and (IMC <= 24.9):
    print ("Status: Normal")
elif (IMC >= 25.0) and (IMC <= 29.9):
    print ("Status: Sobrepeso")
elif (IMC >= 30.0) and (IMC <= 39.9):
    print ("Status: Obesidade")
else:
    print ("Status: Obesidade grave")