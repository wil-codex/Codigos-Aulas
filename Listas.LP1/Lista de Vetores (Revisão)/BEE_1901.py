ordem = int(input())
especies = []

for _ in range(ordem):
    linha = []
    linha = list(map(int, input().split()))
    especies.append(linha)

especie = []
cont = 0
for _ in range(ordem * 2):
    i, j = map(int, input().split())
    novaespecie = especies[i-1][j-1]
    if novaespecie not in especie:
        especie.append(novaespecie)
        cont += 1

print(cont)
    

    
    




    

