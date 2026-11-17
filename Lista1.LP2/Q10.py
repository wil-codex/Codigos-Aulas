from functools import reduce
 
def concatena(palavras):
    print(reduce(lambda a, b: a + " " + b, palavras))
 
concatena(["Resenha", "no", "Clubex"])
 