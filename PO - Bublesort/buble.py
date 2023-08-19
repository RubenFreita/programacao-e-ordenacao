from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    #print(lista)
    return lista
  
mpl.use('Agg')

def bubble_sort(lista):
  ordenado = False
  swaps = 0
  while not ordenado:
    ordenado = True
    for i in range(len(lista)-1):
      if lista[i]>lista[i+1]:
        lista[i], lista[i+1] = lista[i+1], lista[i]
        ordenado = False
        swaps += 1
  lista.append(swaps)
  #print(lista)
  return swaps 



def desenhaGrafico(x,y,label,xl = "Entradas", y1 = "Saídas",nome_arquivo="img"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = label)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(y1)
    plt.xlabel(xl)
    plt.savefig(nome_arquivo)
   
x2 = [10000, 20000, 50000, 100000]
y = []
swaps = []



for i in range(len(x2)):
  tam = geraLista(x2[i])
  y.append(timeit.timeit("bubble_sort({})".format(tam),setup="from __main__ import bubble_sort",number=1))  
  swaps.append(bubble_sort(tam))
  print(x2[i])
 

desenhaGrafico(x2,y, label="Bubblesort",nome_arquivo="GraficoTempo.png", y1="Tempo")
desenhaGrafico(x2,swaps, label="Bubblesort",nome_arquivo="GraficoSwaps", y1="Swaps")
