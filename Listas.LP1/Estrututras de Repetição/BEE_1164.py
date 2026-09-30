n = int(input())

for i in range(n):
    soma = 0
    valor = int(input())

    for j in range(1,valor):
        if valor % j == 0:
            soma += j

    
    if soma == valor:
        print(f"{valor} eh perfeito")
    else:
        print(f"{valor} nao eh perfeito")