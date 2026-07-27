file = 'Memoria-de-XXXII-Jornadas-Academicas.txt'

fil = open(file, 'r')

datos = fil.read()
datos = datos.replace('\n', ' ')
datos = datos.replace(':', '')
datos = datos.replace('.', '')
datos = datos.replace(',', '')
datos = datos.replace(';', '')   
datos = datos.replace('(', '')
datos = datos.replace(')', '')
datos = datos.replace("'", '')
datos = datos.replace('"', '')
datos = datos.replace('#', '')
datos = datos.replace('%', '')
datos = datos.replace('*', '')



datos = datos.split(' ')
datosN = []
for ss in datos:
  ss1 = ss.lower()
  datosN.append(ss1)

datos = datosN
set1 = list(set(datos))

print(len(set1))

set1.sort()

datos = []
for ss in set1:
  tiene_numeros = any(char.isdigit() for char in ss)
  if not tiene_numeros:
    datos.append(ss)

print(datos)



