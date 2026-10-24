precio = float(input("Introduce el precio en euros: "))

euros = int(precio)
centimos = round((precio - euros) * 100)

if centimos == 100:
    euros += 1
    centimos = 0

print(f"Euros: {euros}")
print(f"Céntimos: {centimos:02d}")