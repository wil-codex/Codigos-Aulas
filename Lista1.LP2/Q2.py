def dados_pessoais(**dados):
    partes = []
    if "Nome" in dados:
        partes.append(f"Nome: {dados['Nome']}")
    if "Idade" in dados:
        partes.append(f"Idade: {dados['Idade']}")
    if partes:
        print(" ".join(partes))
 
dados_pessoais(Nome="Júnior", Sobrenome="Limeira", Idade=29, Profissao="Professor")

 