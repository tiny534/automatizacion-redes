# Práctica 05: Mi primer script en Python para la automatización de redes

## Objetivo
Desarrollar un script en Python que permita automatizar la conexión Telnet a un router Cisco y realizar configuraciones de interfaces virtuales y del protocolo de enrutamiento OSPF.

## Herramientas utilizadas
- GNS3.
- Router Cisco IOSv.
- Contenedor NetworkAutomation.
- Python 3.8.5.
- Biblioteca Telnetlib.
- Visual Studio Code.
- Git y GitHub.

## Desarrollo de la práctica
1. Se estableció conectividad entre el contenedor y el router R1.
2. Se configuró el acceso Telnet mediante usuario y contraseña.
3. Se desarrolló el script `python31.py` para automatizar el acceso al router.
4. Se configuró la interfaz Loopback0 con la dirección IP `1.1.1.1/32`.
5. Se agregó la interfaz Loopback1 con la dirección IP `2.2.2.2/32`.
6. Se configuró OSPF mediante el proceso 1, anunciando la red `0.0.0.0 255.255.255.255 area 0`.
7. Se verificaron las interfaces y la configuración OSPF desde la consola de R1.

## Resultados
Se logró automatizar mediante Python la conexión Telnet al router Cisco y la configuración de dos interfaces Loopback. También se aplicó la configuración del protocolo OSPF y se verificaron los resultados desde el router.

## Evidencias
Las capturas de pantalla del desarrollo y los resultados se encuentran en la carpeta `evidencias/`.

## Código fuente
El script de automatización se encuentra en `src/automatizacion_telnet.py`.