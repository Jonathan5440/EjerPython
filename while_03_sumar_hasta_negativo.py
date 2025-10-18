
suma = 0.0
while True:
    try:
        x = float(input("Numero positivo (negativo para terminar): "))
    except ValueError:
        print("Entrada invalida."); continue
    if x < 0: break
    suma += x
print("Suma total:", suma)
