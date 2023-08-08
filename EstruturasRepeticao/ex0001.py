print("Digite dois numeros: ")
a = int(input())
b = int(input())
if a < b:
  print("CRESCENTE!")
elif a > b:
  print("DECRESCENTE!")

while a != b:
  print("Digite dois numeros: ")
  a = int(input())
  b = int(input())
  if a < b:
    print("CRESCENTE!")
  elif a > b:
    print("DECRESCENTE!")

print("PROGRAMA FINALIZADO!")