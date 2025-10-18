
try:
    n = int(input("Numero para su tabla (1-10): "))
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
except ValueError:
    print("Entrada invalida.")
