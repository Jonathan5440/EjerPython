
def es_primo(x):
    if x <= 1: return False
    if x <= 3: return True
    if x % 2 == 0 or x % 3 == 0: return False
    i = 5
    while i*i <= x:
        if x % i == 0 or x % (i+2) == 0: return False
        i += 6
    return True
count = 0
n = 2
while count < 10:
    if es_primo(n):
        print(n); count += 1
    n += 1
