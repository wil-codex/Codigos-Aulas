vetor = []

valor = float(input())

for i in range(100):
    vetor.append(valor)
    valor = valor/2
    print(f"N[{i}] = {vetor[i]:.4f}")