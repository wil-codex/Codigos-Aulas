from functools import reduce
 
def multiplica_for(*numeros):
    resultado = 1
    for n in numeros:
        resultado *= n
    return resultado
 
 
def multiplica_reduce(*numeros):
    return reduce(lambda a, b: a * b, numeros, 1)

print(multiplica_for(2, 3.5, 4))
print(multiplica_reduce(2, 3.5, 4))
 