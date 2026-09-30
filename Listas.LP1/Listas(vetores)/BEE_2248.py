cont = 0
n = int(input())
while True:

    alunos = []
    maior = -1
    cont += 1

    for i in range(n):
        alunos.append(list(map(int, input().split())))
        if alunos[i][1] > maior:
            maior = alunos[i][1]
    aluno = []
    for i in range(n):
        if alunos[i][1] == maior:
            aluno.append(alunos[i][0])
    print(f"Turma {cont}")
    print(*aluno, end=" \n")
    
    n = int(input())    
    if n <= 0:
        break
    print()