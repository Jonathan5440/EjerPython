
try:
    a = float(input("Primer numero: "))
    b = float(input("Segundo numero: "))
    c = float(input("Tercer numero: "))
    mayor = a
    if b > mayor: mayor = b
    if c > mayor: mayor = c
    print("El mayor es:", mayor)
except ValueError:
    print("Entrada invalida.")
