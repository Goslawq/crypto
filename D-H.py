import random

#jawnie ustalone liczby (2 jest mało bezpieczne ale proste obliczeniowo do przedstawianie działania przykładu)
n = 919737126879983098512864719493325177488126658312621992912533
g = 2

# generacja losowych liczb całkowitych
x = random.randrange(2, 100000000000000000000)
y = random.randrange(2, 100000000000000000000)

# generacja kluczy prywatnych
X = pow(g, x, n)
Y = pow(g, y, n)

# generacja klucza sesji
Ak = pow(Y, x, n)
Bk = pow(X, y, n)

print(f"'Ak and Bk are equal statement' is {Ak == Bk}")
size = str(Ak)
size = len(size)
print(f"Length of K is {size} \nand K is equal to {Ak}")
