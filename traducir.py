from deep_translator import GoogleTranslator

# Texto en inglés que quieres traducir
texto_ingles = "Hello, how are you today?"

# Crear el traductor indicando idioma de origen y destino
traductor = GoogleTranslator(source='en', target='es')

# Realizar la traducción
texto_espanol = traductor.translate(texto_ingles)

print("Original:", texto_ingles)
print("Traducido:", texto_espanol)


