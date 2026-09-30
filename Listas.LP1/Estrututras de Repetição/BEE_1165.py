n = int(input())

for _ in range(n):

    valor = int(input())
    contador = 0

    for i in range(1,valor+1):
        if valor % i == 0:
            contador += 1
    if contador == 2:
        print(f"{valor} eh primo")
    else:
        print(f"{valor} nao eh primo")