
try:
    n = int(input("Entero no negativo: "))
    if n < 0:
        print("No existe factorial de negativos.")
    else:
        f = 1
        for i in range(2, n+1):
            f *= i
        print(f"{n}! = {f}")
except ValueError:
    print("Entrada invalida.")
