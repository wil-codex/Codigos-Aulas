n = int(input())
vetor = list(map(int, input().split()))

    
soma = 0
total = sum(vetor)
for i in range(n):
    soma += vetor[i]
    if soma > total/2:
        print(i)
        break

