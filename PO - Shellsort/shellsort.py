from random import shuffle
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
  
mpl.use('Agg')

def geraLista(tam):
  lista = list(range(tam,0,-1))
  shuffle(lista)
  return lista



def shellSort(lista):
    ini = 1
    n = len(lista)
    while ini > 0:
            for i in range(ini, n):
                c = lista[i]
                j = i
                while j >= ini and c < lista[j - ini]:
                    lista[j] = lista[j - ini]
                    j = j - ini
                    lista[j] = c
            ini = int(ini / 2.2)
    return lista

def desenhaGrafico(x,y,xl = "Entradas", y1 = "Saídas",nome_arquivo="img"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Shell Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(y1)
    plt.xlabel(xl)
    plt.savefig(nome_arquivo)


x2 = [100000, 200000, 500000, 1000000, 2000000]
y = []


for i in range(5):
  tam = geraLista(x2[i])
  y.append(timeit.timeit("shellSort({})".format(tam),setup="from __main__ import shellSort",number=1))  
  

desenhaGrafico(x2,y,nome_arquivo="GraficoTempo.png", y1="Saidas")
