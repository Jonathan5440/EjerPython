
try:
    n = int(input("Ingresa un entero positivo: "))
    for d in range(1, n+1):
        if n % d == 0: print(d)
except ValueError:
    print("Entrada invalida.")
