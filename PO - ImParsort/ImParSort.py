def ImParSort(lista):
  par = []
  impar = []
  for i in range(len(lista)):
    if lista[i]%2==0:
      par.append(lista[i])
    else:
      impar.append(lista[i])
  impar = bubble(impar)
  par = bubble(par)
  im = 0 
  p = 0
  arr = []
  for i in range(len(lista)):
    if len(impar) > im and len(par) > p and impar[im] < par[p]:
      arr.append(impar[im])
      im = im + 1
    elif len(impar) > im and len(par) > p and  par[p] < impar[im]:
      arr.append(par[p])
      p = p + 1
  while p < len(par):
    arr.append(par[p])
    p += 1
  while im < len(impar):
    arr.append(impar[im])
    im += 1
  
  return arr


def bubble(arr):

  n = len(arr)

  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j]>arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr
