v = int(input("Quantos numeros voce vai digitar? "))

for i in range(v):
  n = int(input("Digite um número: "))
  if n < 0:
    print("NEGATIVO")
  elif n == 0:
    print("NULO")
  elif n > 0:
    print("POSITIVO")
  else:
    print("VALOR INVÁLIDO")
