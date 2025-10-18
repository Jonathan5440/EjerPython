
suma = 0.0
while suma <= 100:
    try:
        x = float(input("Ingresa un numero: "))
    except ValueError:
        print("Entrada invalida."); continue
    suma += x
    print("Suma:", suma)
print("Supero 100.")
