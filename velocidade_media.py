cidade1 = str(input("Digite o nome do primeiro local: "))
cidade2 = str(input("Digite o nome do segundo local: "))

distancia = float(input(f"Qual a distância entre o local {cidade1} e {cidade2}? (km): "))
tempo_total = float(input(f"Qual o tempo total entre o local {cidade1} e {cidade2}? (horas): "))

velocidade_media = distancia / tempo_total

print (f"A velocidade média gasta no percurso é de: {velocidade_media:.2f} km/h")