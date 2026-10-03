tam = int(input())

for _ in range(tam):

    nAlunos = int(input())
    alunos = list(map(int, input().split()))
    fila = sorted(alunos, reverse=True)

    cont = 0

    for i in range(len(alunos)):
        if alunos[i] == fila[i]:
            cont += 1
    print(cont)
