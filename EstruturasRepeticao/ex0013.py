casos = int(input("Quantos casos voce vai digitar? "))

for i in range(casos):
  print("Digite três números: ")
  a = float(input())
  b = float(input())
  c = float(input())
  media_pond = (a * 2 + b * 3 + c * 5) / 10
  print(f"MÉDIA = {media_pond:.1f}")

