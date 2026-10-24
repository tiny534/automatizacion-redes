productos = input("Introduce los productos de la cesta separados por comas: ")

lista_productos = productos.split(",")

for producto in lista_productos:
    print(producto.strip())