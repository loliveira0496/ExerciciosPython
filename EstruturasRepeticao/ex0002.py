soma = 0
qtd_ind = 0

print("Digite as idades: ")
while True:
    a = int(input())

    if a < 0:
      if qtd_ind == 0:
        print("IMPOSSÍVEL CALCULAR")
      else:
        media = soma / qtd_ind
        print(f"MÉDIA = {media}")
      break
    soma += a
    qtd_ind += 1
