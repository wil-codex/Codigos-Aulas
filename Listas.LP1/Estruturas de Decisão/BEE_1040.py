n1, n2, n3, n4 = map(float, input().split())


media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10

if media >= 7.0:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media < 5.0:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
else:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    nota = float(input())
    print(f"Nota do exame: {nota:.1f}")
    media = (media+nota)/2
    if media >= 5.00:
        print("Aluno aprovado.")
        print(f"Media final: {media:.1f}")
    else:
        print("Alubo reprovado.")