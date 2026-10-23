
# Practica 3: Inventario y busqueda de dispositivos de red

dispositivos = [
    {
        "nombre": "R1",
        "tipo": "Router",
        "ip": "10.1.1.1",
        "loopback": "1.1.1.1",
        "interfaz": "GigabitEthernet0/0",
        "estado": "Activo",
        "fabricante": "Cisco",
        "protocolo": "OSPF"
    },
    {
        "nombre": "R2",
        "tipo": "Router",
        "ip": "10.1.1.2",
        "loopback": "2.2.2.2",
        "interfaz": "GigabitEthernet0/0",
        "estado": "Activo",
        "fabricante": "Cisco",
        "protocolo": "OSPF"
    },
    {
        "nombre": "S1",
        "tipo": "Switch",
        "ip": "10.1.1.3",
        "loopback": "No aplica",
        "interfaz": "Ethernet0/0",
        "estado": "Activo",
        "fabricante": "Cisco",
        "protocolo": "No aplica"
    }
]


def mostrar_dispositivo(dispositivo):
    print("Nombre:", dispositivo["nombre"])
    print("Tipo:", dispositivo["tipo"])
    print("Direccion IP:", dispositivo["ip"])
    print("Loopback:", dispositivo["loopback"])
    print("Interfaz:", dispositivo["interfaz"])
    print("Estado:", dispositivo["estado"])
    print("Fabricante:", dispositivo["fabricante"])
    print("Protocolo:", dispositivo["protocolo"])

    if dispositivo["estado"] == "Activo":
        print("Resultado: El dispositivo esta disponible.")
    else:
        print("Resultado: El dispositivo requiere atencion.")


def buscar_dispositivo(nombre_buscar):
    for dispositivo in dispositivos:
        if dispositivo["nombre"].lower() == nombre_buscar.strip().lower():
            return dispositivo

    return None


print("===== BUSQUEDA DE DISPOSITIVOS =====")

nombre_buscar = input("Ingrese el nombre del dispositivo: ")
resultado = buscar_dispositivo(nombre_buscar)

if resultado is not None:
    print("\nDispositivo encontrado:")
    mostrar_dispositivo(resultado)
else:
    print("No se encontro el dispositivo solicitado.")
