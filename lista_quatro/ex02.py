salario = float(input("Digite o salário bruto (R$): "))
parcela = int(input("Digite o valor mensal da parcela desejada (R$): "))
comprometimento = (parcela / salario) * 100

if parcela > salario * 0.20:
    print(f"Salário bruto: {salario}")
    print(f"Salário bruto: R$ {parcela}")
    print(f"Comprometimento de renda: {comprometimento}% \n")
    print("SOLICITAÇÃO NEGADA: A prestação excede 20% do salário")
else:
    print(f"Salário bruto: R${salario}")
    print(f"Salário bruto: R$ {parcela}")
    print(f"Comprometimento de renda: {comprometimento}% \n")
    print("O valor está dentro do limite permitido")