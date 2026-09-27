idade = int(input())

anos = idade//365
resto = idade % 365
mes = resto//30
resto = resto % 30
dia = resto 

print(f"{anos} ano(s)\n{mes} mes(es)\n{dia} dia(s)")