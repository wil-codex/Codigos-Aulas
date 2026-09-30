n = int(input())            

notas = list(map(int, input().split()))
notas.sort()
maior = notas[0]
cont = 0


for i in range(n):
    if cont <= notas.count(notas[i]):
        conta = notas.count(notas[i])
        maior = notas[i]

print(maior)

    