
try:
    n = int(input("Ingresa un entero: "))
    if n % 5 == 0 and n % 3 == 0:
        print("multiplo de 5 y de 3")
    elif n % 5 == 0:
        print("multiplo de 5")
    elif n % 3 == 0:
        print("multiplo de 3")
    else:
        print("no es multiplo de 5 ni 3")
except ValueError:
    print("Entrada invalida.")
