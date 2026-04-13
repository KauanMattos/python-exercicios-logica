# Crie um programa que:
# - peça 3 notas
# - calcule a média
# - diga:
#   aprovado (>=7)
#   recuperação (>=5 e <7)
#   reprovado (<5)

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceira nota: "))

if n1 > 10 or n1 < 0 or n2 > 10 or n2 < 0 or n3 > 10 or n3 < 0:
    print("Nota Inválida")
    exit() # encerra programa na hora

media = (n1 + n2 + n3) / 3

if media >= 7:
    print("Aprovado")

elif media >=5:
    print("Recuperação")

else:
    print("Reprovado")