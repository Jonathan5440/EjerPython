
print("Ingresa numeros (0 para terminar):")
while True:
    try:
        n = float(input("> "))
    except ValueError:
        print("Entrada invalida."); continue
    if n == 0:
        print("Fin."); break
    print(n)
