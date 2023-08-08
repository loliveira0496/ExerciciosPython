n = int(input("Quantos numeros voce vai digitar? "))

for i in range(n):
    a = int(input("Digite um número: "))
    if a > 0 and a % 2 == 0:
        print("PAR POSITIVO")
    elif a < 0 and a % 2 == 0:
        print("PAR NEGATIVO")
    elif a < 0 and a % 2 != 0:
        print("ÍMPAR NEGATIVO")
    elif a > 0 and a % 2 != 0:
        print("ÍMPAR POSITIVO")
    elif a == 0:
        print("NULO")
    else:
        print("INVÁLIDO")