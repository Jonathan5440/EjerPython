
try:
    n = float(input("Calificacion 0-100: "))
    if n < 0 or n > 100: print("fuera de rango")
    elif n >= 90: print("A")
    elif n >= 80: print("B")
    elif n >= 70: print("C")
    elif n >= 60: print("D")
    else: print("F")
except ValueError:
    print("Entrada invalida.")
