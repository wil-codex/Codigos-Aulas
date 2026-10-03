n = int(input())

fileira = list(map(int, input().split()))

while len(fileira) > 1: 
    novafila = []

    for i in range(len(fileira)-1):
        novafila.append(fileira[i] * fileira[i+1])


    fileira = novafila


if 1 in fileira:
    print('preta')
else:
    print('branca')