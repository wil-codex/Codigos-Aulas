def mais_de_2_digitos(numeros):
    return list(filter(lambda n: len(str(abs(n))) > 2, numeros))
 
 
def programa():
    numeros = [int(input(f"Digite o número {i + 1}: ")) for i in range(6)]
    print("Números com mais de 2 dígitos:", mais_de_2_digitos(numeros))
 
programa()
 