file = 'fmri_jul2726.txt'
file = 'abstract-20260727Da-set.txt'

fil = open(file,'r')

datos = fil.readlines()

nl = len(datos)

listaT = []
lista = []

k = 0
while k < nl:
  ss = datos[k]
  ss = ss.replace('\n', '')
  if len(ss) > 0:
    lista.append(ss)
  else:
    listaT.append(lista)
    lista = []
  k = k+1

nl = len(listaT)

listaN = []

for ss in listaT:
  if len(ss) > 0:
    listaN.append(ss)

i = 0
k = 1
nl = len(listaN)

while i < nl:
  ss = listaN[i]
  ss0 = ss[0]
  if k < 10:
    res = str(k)+'. ' == ss0[:3]
  elif k < 100:
    res = str(k)+'. ' == ss0[:4]
  elif k < 1000:
    res = str(k)+'. ' == ss0[:5]
  else:
    res = str(k)+'. ' == ss0[:6]
  if res:
#    print(ss)
    ss2 = listaN[i+1]
    rr = " ".join(ss2)
    print(str(k)+'. '+rr)
    k = k+1
  i = i+1


