from deep_translator import GoogleTranslator
import sys

def traducir(palabra):
   # Texto en inglés que quieres traducir
   texto_ingles = palabra

   # Crear el traductor indicando idioma de origen y destino
   traductor = GoogleTranslator(source='en', target='es')

   # Realizar la traducción
   texto_espanol = traductor.translate(texto_ingles)
   return texto_espanol

