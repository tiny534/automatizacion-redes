telefono = input("Introduce el teléfono (+52-número-extensión): ")

partes = telefono.split("-")

if len(partes) == 3:
    print("Número de teléfono:", partes[1])
else:
    print("Formato incorrecto. Usa +52-número-extensión.")