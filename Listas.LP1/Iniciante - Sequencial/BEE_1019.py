valor = int(input())

horas = valor//3600
resto = valor % 3600
minutos = resto//60
resto = resto % 60
segundos = resto

print(f"{horas}:{minutos}:{segundos}")
