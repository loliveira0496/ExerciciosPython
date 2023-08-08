while True:
    print("Digite os valores das coordenadas X e Y: ")
    a = int(input())
    b = int(input())

    if a == 0 or b == 0:
        break
    elif a > 0 and b > 0:
        print("QUADRANTE Q1")
    elif a < 0 and b > 0:
        print("QUADRANTE Q2")
    elif a < 0 and b < 0:
        print("QUADRANTE Q3")
    elif a > 0 and b < 0:
        print("QUADRANTE Q4")