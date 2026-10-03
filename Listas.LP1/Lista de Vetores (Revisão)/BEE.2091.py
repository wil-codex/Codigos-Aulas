while True:
    
    teste = int(input())
    if teste < 1:
        break
    lista = list(map(int, input().split()))
    
    for i in range(teste):
        if lista.count() % 2 in lista != 0:
            print(lista[i])
            break


    
