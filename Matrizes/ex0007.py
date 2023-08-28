o = int(input("Qual a ordem da matriz?"))

soma = 0
for i in range(o):
    for j in range(o):
      e = int(input(f"Elemento {[i,j]}: "))
      if i != j and i < j:
         soma += e

print(f"SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {soma}")