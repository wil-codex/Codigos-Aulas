def coordenadas(i, j, k, n):
    return [
        (x, y, z)
        for x in range(i + 1)
        for y in range(j + 1)
        for z in range(k + 1)
        if x + y + z != n
    ]

print(coordenadas(1, 1, 2, 3))
 