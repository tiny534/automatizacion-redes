producto = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
unidades = int(input("Número de unidades: "))

total = precio * unidades

print(
    f"{producto}: precio {precio:09.2f} "
    f"unidades {unidades:03d} "
    f"total {total:011.2f}"
)