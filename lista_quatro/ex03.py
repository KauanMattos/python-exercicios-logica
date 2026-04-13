n1 = float(input("Digite a nota da primeira avaliação (peso 1): "))
n2 = float(input("Digite a nota da segunda avaliação (peso 1): "))
n3 = float(input("Digite a nota da terceira avaliação (peso 2): "))

media = (n1 * 1 + n2 * 1 + n3 * 2) / 4

if media >= 6:
    print("Nota das avaliações:")
    print(f"1ª avaliação (peso 1): {n1}")
    print(f"2ª avaliação (peso 1): {n2}")
    print(f"3ª avaliação (peso 2): {n3} \n")
    print(f"Média final: {media:.1f}")
    print("Status: APROVADO")

else:
    print("Nota das avaliações:")
    print(f"1ª avaliação (peso 1): {n1}")
    print(f"2ª avaliação (peso 1): {n2}")
    print(f"3ª avaliação (peso 2): {n3}\n")
    print(f"Média final: {media:.1f}")
    print("Status: REPROVADO")