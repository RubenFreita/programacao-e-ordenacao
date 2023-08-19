from random import shuffle
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  

mpl.use('Agg')

def geraLista(tam):
  lista = list(range(tam,0,-1))
  shuffle(lista)
  return lista

def heapify(arr, n, i): 
  largest = i   
  l = 2 * i + 1     
  r = 2 * i + 2      
  
     
  if l < n and arr[i] < arr[l]: 
    largest = l 
  
 
  if r < n and arr[largest] < arr[r]: 
    largest = r 
  
    
  if largest != i: 
    arr[i],arr[largest] = arr[largest],arr[i]   
  
        
    heapify(arr, n, largest) 
  

def heapSort(arr): 
  n = len(arr) 
  
     
  for i in range(n, -1, -1): 
    heapify(arr, n, i) 
  
    
  for i in range(n-1, 0, -1): 
    arr[i], arr[0] = arr[0], arr[i]   
    heapify(arr, i, 0)
     
  return arr


def desenhaGrafico(x,y,xl = "Entradas", y1 = "Saídas",nome_arquivo="img"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Lista aleatória")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(y1)
    plt.xlabel(xl)
    plt.savefig(nome_arquivo)


x2 = [100000, 200000, 500000, 1000000, 2000000]
y = []


for i in range(5):
  tam = geraLista(x2[i])
  y.append(timeit.timeit("heapSort({})".format(tam),setup="from __main__ import heapSort",number=1))  
  

desenhaGrafico(x2,y,nome_arquivo="GraficoTempo.png", xl = "Tamanho da Lista", y1="Tempo")
