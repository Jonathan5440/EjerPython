
l = input("Ingresa una letra: ").strip().lower()
if len(l) != 1 or not l.isalpha():
    print("Entrada invalida.")
else:
    print("vocal" if l in "aeiou" else "consonante")
