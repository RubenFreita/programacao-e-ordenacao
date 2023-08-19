from random import shuffle
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  

mpl.use('Agg')

def geraLista(tam):
  lista = list(range(tam,0,-1))
  shuffle(lista)
  return lista

def radixsort(alist):
  ma = max(alist)
  b = 1
  while ma/b > 0:
    ind = len(alist) + 1
    x = [0] * ind
    for i in alist:
      x[i] += 1
      k = 0
      for i in range(ind):
        for j in range(x[i]):
          alist[k] = i
          k += 1
      b *= 10
    
    return alist


def desenhaGrafico(x,y,xl = "Entradas", y1 = "Saídas",nome_arquivo="img"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Lista aleatoria")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(y1)
    plt.xlabel(xl)
    plt.savefig(nome_arquivo)


x2 = [100000, 200000, 500000, 1000000, 2000000]
y = []


for i in range(5):
  tam = geraLista(x2[i])
  y.append(timeit.timeit("radixsort({})".format(tam),setup="from __main__ import radixsort",number=1))  
  

desenhaGrafico(x2,y,nome_arquivo="GraficoTempo.png", xl = "Tamanho da Lista", y1="Tempo")
