
try:
    n = int(input("Ingresa n: "))
    print(sum(range(2, n+1, 2)))
except ValueError:
    print("Entrada invalida.")
