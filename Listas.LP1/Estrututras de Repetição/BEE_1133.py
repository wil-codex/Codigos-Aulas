x = int(input())
y = int(input())

inicio = min(x,y)
fim = max(x,y)

for i in range(inicio+1, fim):
    if i % 5 == 3 or i % 5 == 2:
        print(i)