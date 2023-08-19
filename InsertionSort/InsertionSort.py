from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista
  
mpl.use('Agg')

def geraListaPior(tam):
  lista=[]
  ind = tam
  for i in range(tam):
    lista.append(ind)
    ind -=1
  return lista


def insertionSort(lista):
  cont=0
  for i in range(len(lista)):
    temp = lista[i]
    j = i
    while j>0 and temp<lista[j-1]:
      cont+=1
      lista[j] = lista[j-1]
      j -= 1
    lista[j] = temp
  return cont


def desenhaGrafico(x,y,y2,xl = "Entradas", y1 = "Saídas",nome_arquivo="img"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Insertion Aleatorio")
    ax.plot(x,y2, label = "Insertion Pior Caso")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(y1)
    plt.xlabel(xl)
    plt.savefig(nome_arquivo)
   
x2 = [10000, 20000, 50000, 100000]
y = []
y2 = []
cont = []
cont1 = []

for i in range(4):
  x = x2[i]
  tam = geraLista(x2[i])
  tam1 = geraListaPior(x2[i])
  y.append(timeit.timeit("insertionSort({})".format(tam),setup="from __main__ import insertionSort",number=1))  
  cont.append(insertionSort(tam))
  y2.append(timeit.timeit("insertionSort({})".format(tam1),setup="from __main__ import insertionSort",number=1))
  cont1.append(insertionSort(tam1))
  print(x)
 
desenhaGrafico(x2,y,y2,nome_arquivo="GraficoTempo.png", y1="Tempo")
desenhaGrafico(x2,cont,cont1,nome_arquivo="GraficoComparacoes.png", y1="Comparacoes")
