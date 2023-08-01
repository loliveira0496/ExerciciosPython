hi = int(input("Hora inicial: "))
hf = int(input("Hora final: "))

if hi > hf:
  d = 24 - hi + hf
elif hi < hf:
  d = hf - hi

print(f"O JOGO DUROU {d} HORAS")