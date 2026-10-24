precio_habitual = 3.49
descuento = 0.60

barras = int(input("Número de barras que no son del día: "))

descuento_barra = precio_habitual * descuento
precio_final = precio_habitual - descuento_barra
total = precio_final * barras

print(f"Precio habitual por barra: ${precio_habitual:.2f}")
print(f"Descuento por barra: ${descuento_barra:.2f}")
print(f"Precio con descuento por barra: ${precio_final:.2f}")
print(f"Coste final total: ${total:.2f}")