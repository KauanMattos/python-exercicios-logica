n1 = float(input("Digite a primeira nota (0.0 a 10.0):  "))
n2 = float(input("Digite a segunda nota (0.0 a 10.0):  "))

if 0 < n1 > 10 or 0 < n2 > 10:
    print("ERRO: As notas devem estar no intervalo de 0.0 a 10.0")

else:
    media = (n1 + n2) / 2
    print(f"Média aritmética: {media:.1f}")