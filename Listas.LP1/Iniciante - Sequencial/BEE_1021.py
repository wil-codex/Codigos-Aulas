valor = float(input())* 100

#estrutura de contagem
nota100 = valor//10000
resto = valor % 10000

nota50 = resto//5000
resto = resto % 5000

nota20 = resto//2000
resto = resto % 2000

nota10 = resto//1000
resto = resto % 1000

nota5 = resto//500
resto = resto % 500

nota2 = resto//200
resto = resto % 200

moeda1 = resto//100
resto = resto % 100

moeda50 = resto//50
resto = resto % 50

moeda25 = resto//25
resto = resto % 25

moeda10 = resto//10 
resto = resto % 10

moeda5 = resto//5
resto = resto % 5

moeda01 = resto

print(f"{nota100} notas(s) de R$ 100.00")
print(f"{nota50} notas(s) de R$ 50.00")
print(f"{nota20} notas(s) de R$ 20.00")
print(f"{nota10} notas(s) de R$ 10.00")
print(f"{nota5} notas(s) de R$ 5.00")
print(f"{nota2} notas(s) de R$ 2.00")


print(f"{moeda1} moeda(s) de R$ 1.00")
print(f"{moeda50} moeda(s) de R$ 0.50")
print(f"{moeda25} moeda(s) de R$ 0.25")
print(f"{moeda10} moeda(s) de R$ 0.10")
print(f"{moeda5} moeda(s) de R$ 0.05")
print(f"{moeda01} moeda(s) de R$ 0.01")




