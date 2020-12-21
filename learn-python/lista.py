import random

lista = [] 

for x in range(1, 21):
    lista.append(random.randint(1, 10))

media = 0.0
soma = 0

for i in lista:
    soma += i

print(lista)
media = soma / 100
print("Media = ", media)

num = int(input("Numero: "))

k = 0

for i in lista:
    if i == num:
        k += 1

print("Ocorrencias: ", k)
