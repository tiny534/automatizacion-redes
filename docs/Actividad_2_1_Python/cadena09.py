fecha = input("Introduce una fecha (dd/mm/aaaa): ")

partes = fecha.split("/")

if len(partes) == 3:
    dia = int(partes[0])
    mes = int(partes[1])
    anio = partes[2]

    print(f"Día: {dia}")
    print(f"Mes: {mes}")
    print(f"Año: {anio}")
else:
    print("Formato incorrecto. Usa dd/mm/aaaa.")