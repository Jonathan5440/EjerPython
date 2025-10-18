
try:
    n = int(input("Ingresa un entero positivo: "))
    i = 2
    while i <= n:
        print(i)
        i += 2
except ValueError:
    print("Entrada invalida.")
