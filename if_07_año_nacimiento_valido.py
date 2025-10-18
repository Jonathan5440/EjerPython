
from datetime import datetime
try:
    anio = int(input("Ingresa tu anio de nacimiento: "))
    actual = datetime.now().year
    print("valido" if 1900 < anio < actual else "no valido")
except ValueError:
    print("Entrada invalida.")
