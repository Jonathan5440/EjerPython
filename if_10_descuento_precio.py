
try:
    precio = float(input("Precio del articulo: "))
    descuento = float(input("Descuento en %: "))
    if precio < 0 or descuento < 0 or descuento > 100:
        print("Datos fuera de rango.")
    else:
        final = precio * (1 - descuento/100)
        print(f"Precio final: {final:.2f}")
except ValueError:
    print("Entrada invalida.")
