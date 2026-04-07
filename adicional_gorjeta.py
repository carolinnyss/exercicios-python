gastos = float(input("Qual foi o valor gasto no restaurante? R$ "))
taxa_gorjeta = float(input("Qual a porcentagem da gorjeta? (Ex.: 10 para 10%): "))
taxagarçom = gastos * (1 + taxa_gorjeta / 100)

print (f"O valor total da conta com a gorjeta ficou R$ {taxagarçom:.2f}")