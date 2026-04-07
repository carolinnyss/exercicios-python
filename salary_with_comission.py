salario = float(input("Digite seu salário atual R$ "))
comissao = float(input("Digite a porcentagem da comissão (Ex.: 10 para 10%): "))

if comissao >= 1:
    comissao = comissao / 100

formula_comissao = salario * comissao
salario_atual = formula_comissao + salario

print (f"O seu salário com comissão é: {salario_atual:.2f}")