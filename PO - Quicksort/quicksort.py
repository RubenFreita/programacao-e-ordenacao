from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
  
mpl.use('Agg')

def geraLista(tam):
  return list(range(tam, 0, -1))


def quickSort(lista):
  esq = []
  equal = []
  dire = []
  if len(lista)>1:
    pivot = lista[len(lista)//2]
    for i in lista:
      if i<pivot:
        esq.append(i)
      elif i>pivot:
        dire.append(i)
      elif i==pivot:
        equal.append(i)
    return quickSort(esq) + equal + quickSort(dire)
  return lista


def desenhaGrafico(x,y,xl = "Entradas", y1 = "Saídas",nome_arquivo="img"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "QUICK SORT")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(y1)
    plt.xlabel(xl)
    plt.savefig(nome_arquivo)

x2 = [100000, 200000, 500000, 1000000, 2000000]
y = []


for i in range(5):
  tam = geraLista(x2[i])
  y.append(timeit.timeit("quickSort({})".format(tam),setup="from __main__ import quickSort",number=1))  
  

desenhaGrafico(x2,y,nome_arquivo="GraficoTempo.png", y1="Tempo")
