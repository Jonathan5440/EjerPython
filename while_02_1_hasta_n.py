
try:
    n = int(input("Ingresa un entero positivo: "))
    i = 1
    while i <= n:
        print(i)
        i += 1
except ValueError:
    print("Entrada invalida.")
