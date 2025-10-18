
suma = 0.0; cont = 0
print("Ingresa numeros (0 para terminar):")
while True:
    try:
        x = float(input("> "))
    except ValueError:
        print("Entrada invalida."); continue
    if x == 0: break
    suma += x; cont += 1
print("Sin datos" if cont == 0 else f"Media: {suma/cont}")
