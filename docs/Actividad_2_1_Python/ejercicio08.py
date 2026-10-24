
n = int(input("Introduce el primer número entero: "))
m = int(input("Introduce el segundo número entero: "))

if m != 0:
    cociente = n // m
    resto = n % m
    print(f"{n} entre {m} da un cociente {cociente} y un resto {resto}")
else:
    print("No se puede dividir entre cero.")
