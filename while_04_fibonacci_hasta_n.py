
try:
    limite = int(input("Generar Fibonacci hasta (valor maximo): "))
    a,b = 0,1
    while a <= limite:
        print(a)
        a,b = b, a+b
except ValueError:
    print("Entrada invalida.")
