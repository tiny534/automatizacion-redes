correo = input("Escribe tu correo electrónico: ")

if "@" in correo:
    usuario = correo.split("@")[0]
    nuevo_correo = usuario + "@utmatamoros.edu.mx"
    print("Nuevo correo:", nuevo_correo)
else:
    print("El correo no tiene un formato válido.")