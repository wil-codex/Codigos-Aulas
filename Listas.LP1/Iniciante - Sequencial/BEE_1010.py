peca = list(input().split())
compra1 = peca
peca = list(input().split())
compra2 = peca

print(f"VALOR A PAGAR: R% {(int(compra1[1])*float(compra1[2])+int(compra2[1])*float(compra2[2])):.2f}")