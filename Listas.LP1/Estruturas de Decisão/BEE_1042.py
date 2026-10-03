v1, v2, v3 = map(int, input().split())


if v1 > v2 and v1 > v3 and v2 > v3:
    maior, meio, menor = v1, v2, v3
elif v3 > v2 and v3 > v1:
    if v1 > v2:
        maior, meio, menor = v3, v1, v2
    else: 
        maior, meio, menor = v3, v2, v1
elif v2 > v1 and v2 > v3:
    if v3 > v1:
        maior, meio, menor = v2, v3, v1
    else:
        maior, meio, menor = v2, v1, v3

print(f"{menor}\n{meio}\n{maior}")
print()
print(f"{v1}\n{v2}\n{v3}")






