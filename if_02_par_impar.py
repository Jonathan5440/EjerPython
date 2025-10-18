
try:
    n = int(input("Ingresa un entero: "))
    print("par" if n % 2 == 0 else "impar")
except ValueError:
    print("Entrada invalida.")
