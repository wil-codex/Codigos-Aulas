n = int(input())

valor1 = 0
valor2 = 1
print(valor1)
print(valor2)

for i in range(n-2):
    prox = valor1 + valor2
    valor1 = valor2
    valor2 = prox
    print(prox)
    