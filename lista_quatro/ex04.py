print("=== CALCULADORA ====")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Sair\n")

opcao = int(input("Escolha uma opção (1-5): "))

if opcao == 1:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    resultado = n1 + n2
    print(f"\nResultado: {n1} + {n2} = {resultado}")

elif opcao == 2:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    resultado = n1 - n2
    print(f"\nResultado: {n1} - {n2} = {resultado}")

elif opcao == 3:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    resultado = n1 * n2
    print(f"\nResultado: {n1} * {n2} = {resultado}")

elif opcao == 4:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if n2 == 0:
        print("\nERRO: Divisão por zero não é permitida!\n")
        exit()
    else:
        resultado = n1 / n2
        print(f"\nResultado: {n1} / {n2} = {resultado}")

elif opcao == 5:
    print("\nSaindo da Calculadora..\n")

else:
    print("Opção Inválida! Tente Novamente\n")