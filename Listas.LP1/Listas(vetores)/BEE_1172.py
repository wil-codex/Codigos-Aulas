vetor = []
for i in range(10):
    valor = int(input())
    vetor.append(valor)
    if vetor[i] > 0:
        print(f"X[{i}] = {vetor[i]}")
    else: 
        print(f"X[{i}] = 1")