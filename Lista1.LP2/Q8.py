def letras_palavras(frase):
    vogais = "aeiouáéíóúâêôãõàAEIOUÁÉÍÓÚÂÊÔÃÕÀ"
 
    def letras(palavra):
        qtd_vogais = len([c for c in palavra if c in vogais])
        return f"{palavra}: tamanho = {len(palavra)}, vogais = {qtd_vogais}"
 
    for linha in map(letras, frase.split()):
        print(linha)
 
letras_palavras("Resenha no clube")
 