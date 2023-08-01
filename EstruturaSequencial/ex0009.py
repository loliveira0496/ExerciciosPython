# Digitar a duração de tempo em segundos
d = int(input("Digite a duracao em segundos: "))
# Converter essa duração para o formato de horas: minutos: segundos.
if d < 60:
    s = d
else:
    s = d % 60

m = (d % 3600) // 60
h = d // 3600

print(f"{h}:{m}:{s}")

