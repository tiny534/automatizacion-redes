frase = input("Escribe una frase: ")
vocal = input("Escribe una vocal: ").lower()

if vocal in "aeiou" and len(vocal) == 1:
    frase_modificada = frase.replace(vocal, vocal.upper())
    print("Frase modificada:", frase_modificada)
else:
    print("Debes escribir una sola vocal.")