a, b, c = map(float, input().split())

aTriangulo = a*c 
aCirculo = (c**2)*3.14159
aTrapezio = ((a+b)*c)/2
aQuadrado = b*b
aRetangulo = a*b

print(f"TRIANGULO: {aTriangulo:.3f}\nCIRCULO: {aCirculo:.3f}\nTRAPÉZIO: {aTrapezio:.3f}\nQUADRADO: {aQuadrado:.3f}\nRETANGULO: {aRetangulo:.3f}")
