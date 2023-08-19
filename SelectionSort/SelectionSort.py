from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    print(lista)
    return lista
  
mpl.use('Agg')

def selectionSort(lista):
  cont = 0

  for i in range(len(lista)):
    
    minPos = i
    

    for j in range(i+1, len(lista)):
      
      
      if lista[minPos] > lista[j]:
        cont += 1
        minPos = j
       
    lista[i], lista[minPos] = lista[minPos], lista[i]
  print(lista)
  return cont

def selectionSortP(lista):

  for i in range(len(lista)):
    
    minPos = i
    

    for j in range(i+1, len(lista)):
      
      
      if lista[minPos] < lista[j]:
        minPos = j
       
    lista[i], lista[minPos] = lista[minPos], lista[i]
  print(lista)
  return lista





def desenhaGrafico(x,y,y2,xl = "Entradas", y1 = "Saídas",nome_arquivo="img"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Selection Aleatorio")
    ax.plot(x,y2, label = " Selection Pior Caso")
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
  tam = geraLista(x2[i])
  tam1 = selectionSortP(geraLista(x2[i]))
  y.append(timeit.timeit("selectionSort({})".format(tam),setup="from __main__ import selectionSort",number=1))  
  cont.append(selectionSort(tam))
  y2.append(timeit.timeit("selectionSort({})".format(tam1),setup="from __main__ import selectionSort",number=1))
  cont1.append(selectionSort(tam1))
  
  
desenhaGrafico(x2,y,y2,nome_arquivo="GraficoTempo.png", y1="Tempo")
desenhaGrafico(x2,cont,cont1,nome_arquivo="GraficoComparacoes.png", y1="Comparacoes")
