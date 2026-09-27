p1, c1, p2, c2 = map(int, input().split())

esquerda = p1 * c1
direita = p2 * c2

print((direita > esquerda) - (esquerda > direita))

