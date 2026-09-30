n = int(input())
vetor = list(map(int, input().split()))

indice = 0
for i in range(n-1):
    if vetor[i+1] < vetor[i]:
        indice = i + 2
        break
print(indice)