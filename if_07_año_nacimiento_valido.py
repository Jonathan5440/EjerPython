
from datetime import datetime
try:
    año = int(input("Ingresa tu año de nacimiento: "))
    actual = datetime.now().year
    print("valido" if 1900 < año < actual else "no valido")
except ValueError:
    print("Entrada invalida.")
