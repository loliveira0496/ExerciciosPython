mg = float(input("Digite a medida da glicose: "))

if mg > 0 and mg < 100:
  print("Classificação: normal")
elif mg > 100 and mg <= 140:
  print("Classificação: elevado")
elif mg > 140:
  print("Classificação: diabetes")
else:
  print("Valor inválido")

