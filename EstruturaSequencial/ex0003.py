print("Dados da primeira pessoa: ")
n1 = input("Nome: ") 
age = float(input("Idade: ")) 
print("Dados da primeira pessoa: ")
n2 = input("Nome: ") 
age2 = float(input("Idade ")) 

media_idade = (age + age2)/2

print(f"A idade média de {n1} e {n2} é de {media_idade}")

print("A idade média de {} e {} é de {}".format(n1, n2, media_idade))

print("A idade média de %s e %s é de %.1f" % (n1, n2, media_idade))

