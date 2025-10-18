
try:
    n = int(input("Cantidad de terminos: "))
    s = 0
    for i in range(1, n+1):
        s += i
        print(s)
except ValueError:
    print("Entrada invalida.")
