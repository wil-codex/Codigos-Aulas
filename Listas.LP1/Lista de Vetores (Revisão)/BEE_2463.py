tam = int(input())

corredor = list(map(int, input().split()))
soma_atual = 0
maior_soma = 0
for i in range(len(corredor)):

    soma_atual += corredor[i]
    if soma_atual < 0:
        soma_atual = 0

    if soma_atual > maior_soma:
        maior_soma = soma_atual


print(maior_soma)