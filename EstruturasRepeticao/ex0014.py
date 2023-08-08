casos = int(input("Quantos casos voce vai digitar? "))

for i in range(casos):
  print("Entre com o numerador: ")
  a = float(input())
  print("Entre com o denominador: ")
  b = float(input())
  if b == 0:
    print("DIVISÃO IMPOSSÍVEL")
  div = a / b
  
  print(f"DIVISÃO = {div:.2f}")
