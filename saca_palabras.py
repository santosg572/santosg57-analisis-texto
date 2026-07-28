file = 'titulos_pubmed.txt'

fil = open(file, 'r')

datos = fil.read()

datos = datos.replace('\n', ' ')
datos = datos.replace('.', '')
datos = datos.replace(':', '')
datos = datos.replace(',', '')
datos = datos.replace(';', '')
datos = datos.replace(')', '')
datos = datos.replace('(', '')
datos = datos.replace('(', '')
datos = datos.replace('+/-', '')
datos = datos.replace('(', '')
datos = datos.replace('(', '')
datos = datos.replace('(', '')



dd = datos.split(' ')

set1 = list(set(dd))

lista = []

for ss in set1:
  if len(ss) > 2:
    tt = any(c.isdigit() for c in ss)
    if not tt:
      lista.append(ss.lower())

set2 = list(set(lista))

set2.sort()

print(set2)

