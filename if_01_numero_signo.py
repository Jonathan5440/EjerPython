
def clasificar_numero(n):
    if n > 0: return "positivo"
    if n < 0: return "negativo"
    return "cero"
if __name__ == "__main__":
    try:
        n = float(input("Ingresa un numero: "))
        print("El numero es", clasificar_numero(n))
    except ValueError:
        print("Entrada invalida.")
