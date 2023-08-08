while True:
  a = float(input("Digite a primeira nota: "))
  while a < 0 or a > 10:
    print("Valor inválido! Tente novamente!")
    a = float(input("Digite a primeira nota: "))

  b = float(input("Digite a segunda nota: "))
  while b < 0 or b > 10:
    print("Valor inválido! Tente novamente!")
    b = float(input("Digite a segunda nota: "))
    
  media = (a + b) / 2
  print(f"MÉDIA = {media:.2f}")
  break