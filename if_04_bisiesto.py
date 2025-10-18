
def es_bisiesto(a):
    return (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)
try:
    a = int(input("Anio: "))
    print("bisiesto" if es_bisiesto(a) else "no bisiesto")
except ValueError:
    print("Entrada invalida.")
