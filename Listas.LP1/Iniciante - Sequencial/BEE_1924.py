n =  int(input())
cursos = []

for i in range(3):
    curso = input()
    cursos.append(curso)
    if cursos[i] == 'Ciencia da Computacao':
        print(cursos[i])
        break
    
