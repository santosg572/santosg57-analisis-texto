file = 'Memoria-de-XXXII-Jornadas-Academicas.txt'

fil = open(file, 'r')

datos = fil.readlines()

i = 1
nl = len(datos)
k=1
while k < nl:
  ss = datos[k]
  ss = ss.replace('\n', '')
  if str(i)+'.-' in ss:
    print(ss)
    k = k+1
    print(datos[k])
    k = k+1
    print(datos[k])
    i = i+1
  k = k+1
