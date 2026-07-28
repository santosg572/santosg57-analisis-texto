import funcion_traducir as trad

file = 'palabras.txt'

fil = open(file,'r')

datos = fil.read()

datos = datos.replace('\n', ' ')
datos = datos.replace("'", '')
datos = datos.replace(",", '')
datos = datos.replace("[", '')
datos = datos.replace("]", '')

#print(datos)

dd = datos.split(' ')

print(len(dd))

k = 1
for ss in dd:
#  print(ss)
  if len(ss) > 2:
    print(ss)
    ss1 = trad.traducir(ss)
    sst = str(k)+'. ' + ss + ' ------ ' +ss1
    print(sst)
    k = k+1
