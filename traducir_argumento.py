from deep_translator import GoogleTranslator
import sys

# Texto en inglés que quieres traducir
texto_ingles = sys.argv[1]

# Crear el traductor indicando idioma de origen y destino
traductor = GoogleTranslator(source='en', target='es')

# Realizar la traducción
texto_espanol = traductor.translate(texto_ingles)

print("Original:", texto_ingles)
print("Traducido:", texto_espanol)


