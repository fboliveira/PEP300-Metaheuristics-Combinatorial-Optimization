import numpy as np
import random
from copy import deepcopy

def inicial(x):
    
    if x < 10:
        print("O valor é menor que 10")
    elif x >= 10 and x < 20:
        print("O valor está entre 10 e 20")
    else:
        print("O valor é maior ou igual a 20")


    i = 0

    while i < 10:
        print(i)
        i += 1

    for i in range(10, 20):
        print(i)

    # foreach
    a = [5, 3, 8, 1, 2]

    for x in a:
        print(x)

    w = 3
    k = 20

    return w, k

def lerArquivo(arquivo):

    dados = open(arquivo)

    for linha in dados:
        print(linha)

    dados.close()

def lista():

    a = list(range(1, 11))
    random.shuffle(a)

    b = deepcopy(a)

    print(a)

    a.append(15)
    a.remove(5)

    print(a)
    print(b)



def matriz():

    m = np.zeros(shape=(5, 5), dtype=int)
    
    m[0][0] = 5

    print(m)
    print(m[0][:])




def main():
    # x, y = inicial(25)
    # print(x, y)
    # matriz()
    lista()

main()