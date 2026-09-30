tam = int(input())
vetor = list(map(int, input().split()))

for i in range(tam):
    if not i:
        menor = vetor[i]
    if vetor[i] < menor:
        menor = vetor[i]

print(f"Menor valor: {menor}\nPosicao: {vetor.index(menor)}")

