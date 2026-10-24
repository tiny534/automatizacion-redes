
deposito = float(input("Cantidad depositada en la cuenta: $"))

saldo = deposito

for anio in range(1, 4):
    saldo = saldo * 1.04
    print(f"Ahorros después del año {anio}: ${saldo:.2f}")
