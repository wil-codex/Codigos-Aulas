tam, cap = map(int, input().split())

pessoas = 0
ultrapassou = False


for _ in range(tam):
    s, e = map(int, input().split())
    pessoas += e-s
    if pessoas > cap:
        ultrapassou = True

if ultrapassou:
    print('S')
else:
    print('N')

        

    
    
