from random import shuffle
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  

mpl.use('Agg')

def geraLista(tam):
  lista = list(range(tam,0,-1))
  shuffle(lista)
  return lista


def gnomeSort( arr): 
  n = len(arr)
  index = 0
  while index < n: 
    if index == 0: 
      index = index + 1
    if arr[index] >= arr[index - 1]: 
      index = index + 1
    else: 
      arr[index], arr[index-1] = arr[index-1], arr[index] 
      index = index - 1
  print(len(arr))
  return arr

def desenhaGrafico(x,y,xl = "Entradas", y1 = "Saídas",nome_arquivo="img"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Lista aleatória no GnomeSort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(y1)
    plt.xlabel(xl)
    plt.savefig(nome_arquivo)


x2 = [10000, 20000, 50000, 100000, 200000]
y = []


for i in range(5):
  tam = geraLista(x2[i])
  y.append(timeit.timeit("gnomeSort({})".format(tam),setup="from __main__ import gnomeSort",number=1))  
  

desenhaGrafico(x2,y,nome_arquivo="GraficoTempo.png", xl = "Tamanho da Lista de entrada", y1="Tempo")
