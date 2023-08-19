from random import shuffle
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
  
mpl.use('Agg')

def geraLista(tam):
  lista = list(range(tam,0,-1))
  shuffle(lista)
  return lista

def bucket_sort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])
 
    for i in range(length):
        quickSort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
    print(result)
    return result
 
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
    ax.plot(x,y, label = "Bucket Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(y1)
    plt.xlabel(xl)
    plt.savefig(nome_arquivo)


x2 = [100000, 200000, 500000, 1000000, 2000000]
y = []


for i in range(5):
  tam = geraLista(x2[i])
  y.append(timeit.timeit("bucket_sort({})".format(tam),setup="from __main__ import bucket_sort",number=1))  
  

desenhaGrafico(x2,y,nome_arquivo="GraficoTempo.png", y1="Saidas")
