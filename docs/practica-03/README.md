# Práctica 3. Primer programa de Python para representar información de dispositivos

## 1. Propósito

El propósito de esta práctica fue desarrollar un programa en Python para representar y organizar información de los dispositivos de una infraestructura de red simulada en GNS3. Se utilizaron variables, diccionarios, listas, ciclos, condiciones y funciones para mostrar y buscar información de los equipos.

## 2. Conceptos utilizados

- **Variables:** permiten almacenar información como el nombre, tipo, dirección IP y estado de un dispositivo.
- **Tipos de datos:** se utilizaron cadenas de texto (`str`) para representar los datos de los equipos.
- **print():** permite mostrar la información en la terminal.
- **Diccionarios:** agrupan los datos de cada dispositivo mediante claves y valores.
- **Listas:** permiten almacenar varios dispositivos dentro de una misma estructura.
- **Ciclo for:** recorre la lista y procesa cada dispositivo.
- **Condicional if:** comprueba el estado de cada equipo y muestra un mensaje según el resultado.
- **Funciones:** permiten reutilizar instrucciones para mostrar y buscar dispositivos.

## 3. Dispositivos representados

| Dispositivo | Tipo | Dirección IP | Estado | Función |
|---|---|---|---|---|
| R1 | Router | 10.1.1.1 | Activo | Enrutamiento |
| R2 | Router | 10.1.1.2 | Activo | Enrutamiento |
| S1 | Switch | 10.1.1.3 | Activo | Conectividad |

*Nota: las direcciones y los datos de esta tabla son ejemplos. Deben ajustarse a la topología configurada en GNS3.*

## 4. Evidencias

Las capturas de pantalla de la práctica se guardarán en la carpeta `evidencias`.

1. Evidencia 1: estructura del repositorio.
2. Evidencia 2: código fuente del programa.
3. Evidencia 3: ejecución del programa.
4. Evidencia 4: representación de R1 y R2.
5. Evidencia 5: uso de listas y diccionarios.
6. Evidencia 6: ejecución de varios dispositivos.
7. Evidencia 7: uso de condiciones y funciones.
8. Evidencia 8: búsqueda de dispositivos por nombre.
9. Evidencia 9: documentación de la práctica.
10. Evidencia 10: problemas y soluciones.
11. Evidencia 11: actualización del README principal.
12. Evidencia 12: repositorio actualizado en GitHub.

## 5. Problemas y soluciones

| Problema | Causa | Solución |
|---|---|---|
| Organización inicial de los datos | Los datos estaban separados en variables | Se agruparon mediante diccionarios |
| Mostrar varios dispositivos | Era necesario repetir instrucciones | Se utilizó una lista y un ciclo `for` |
| Identificar dispositivos fuera de servicio | Se necesitaba evaluar el estado | Se incorporó una condición `if` |

## 6. Preguntas de análisis

### 1. ¿Por qué es útil representar la información de los dispositivos mediante un programa?

Porque permite almacenar y consultar los datos de los equipos de forma organizada, facilitando la administración de una red.

### 2. ¿Qué ventaja ofrece utilizar un diccionario para representar un dispositivo?

Permite agrupar todos los datos de un dispositivo mediante claves, haciendo más sencilla su consulta y modificación.

### 3. ¿Qué ventaja ofrece utilizar una lista para representar varios dispositivos?

Permite guardar varios equipos en una misma estructura y procesarlos sin tener que escribir instrucciones separadas para cada uno.

### 4. ¿Qué tarea permite realizar el ciclo for?

Permite recorrer la lista de dispositivos y ejecutar las mismas instrucciones para cada elemento.

### 5. ¿Para qué se utilizó la estructura if?

Para comprobar el estado registrado de cada dispositivo y mostrar un mensaje según estuviera activo o requiriera atención.

### 6. ¿Qué ventaja tiene utilizar una función?

Permite reutilizar código, evitar repeticiones y mantener el programa más organizado.

### 7. ¿Qué información de los dispositivos podría obtener automáticamente un programa en una etapa posterior?

Podría obtener direcciones IP, interfaces, estado de las conexiones, tablas de enrutamiento y otros datos disponibles mediante las herramientas de administración de red.

### 8. ¿Qué diferencia existe entre representar información de un dispositivo y obtener esa información directamente desde el dispositivo?

Representarla consiste en escribir los datos manualmente en el programa. Obtenerla directamente requiere establecer una conexión y consultar el equipo real o simulado mediante herramientas de automatización.

### 9. ¿Cómo podría evolucionar este programa para convertirse en una herramienta de automatización de redes?

Se podrían agregar bibliotecas de Python para conectarse a los equipos, consultar su configuración, comprobar su estado y ejecutar tareas automatizadas.

### 10. ¿Qué relación existe entre esta práctica, la Práctica 2 y las siguientes prácticas del proyecto integrador?

La Práctica 2 permitió construir la infraestructura simulada en GNS3. En esta práctica se representó su información con Python. En las siguientes se podrá avanzar hacia la consulta y automatización de los dispositivos.

## 7. Conclusión individual

En esta práctica aprendí a utilizar Python para representar información de dispositivos de red. También aprendí a trabajar con variables, diccionarios y listas para organizar los datos. Utilicé el ciclo `for` para mostrar varios dispositivos sin repetir tantas instrucciones. Con la condición `if` pude identificar el estado registrado de cada equipo. Además, creé funciones para mostrar y buscar dispositivos por su nombre. Una de las dificultades fue organizar toda la información en el código, pero la resolví agrupando los datos mediante diccionarios. Comprendí que Python puede ayudar a administrar una infraestructura de red de forma más ordenada. En las siguientes etapas, este programa podría ampliarse para consultar dispositivos y automatizar tareas de red.

## 8. Problemas encontrados

Durante el desarrollo se comprobó la ejecución del programa y se organizaron los datos mediante estructuras de Python. Los problemas adicionales que se presenten se registrarán en esta sección con su causa y solución.

## 9. Resultado final

Se desarrolló un programa en Python que representa tres dispositivos de ejemplo, muestra su información, comprueba su estado registrado y permite buscar un equipo por nombre. La conexión real con los dispositivos de GNS3 queda pendiente para las siguientes prácticas.