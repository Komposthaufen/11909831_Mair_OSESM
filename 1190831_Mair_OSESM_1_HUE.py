
import numpy as np

v_1 = 100
v_2 = 20

# Überschreibung von Variablen
v_1 = v_2

# Ausgabe einer Variable
print("Wert von Variable 1:", v_1)
print("\n")

# Definition über liste
z = [1.1, 2.2, 3.3]
vec1 = np.array(z)
print(vec1)
print("Dimensionen:", np.shape(z))
print("Länge der Liste:", len(z))

# Mehrdimensionale Matrix
y = [[2.9], [2.3], [3.6]]  # Liste von Listen
vec2 = np.array(y)
print(vec2)
print("Dimensionen:", np.shape(y))

# Rechnungen
Summe = v_1 + v_2
Produkt = v_1 * v_1
Sub = v_1 - v_1
Div = v_1 / v_1
Pot = v_1 ** v_1

print("Summe:", Summe)
print("Produkt:", Produkt)
print("Sub:", Sub)
print("Div:", Div)
print("Pot:", Pot)


#4 Funktionen
def factorial(n):
    #Calculate the factorial of a non-negative integer.
    return 1 if n == 0 else n * factorial(n-1)


def is_prime(n):
    #Check if a number is prime.
    if n <= 1: return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def is_even(n):
    #Check if a number is even.
    return n % 2 == 0


def is_odd(n):
    #Check if a number is odd.
    return n % 2 != 0


# Calling the  functions with v_1
v_1_factorial = factorial(v_1)
v_1_is_prime = is_prime(v_1)
v_1_even = is_even(v_1)
v_1_odd = is_odd(v_1)

print("Faktorial:", v_1_factorial)
print("IsPrime:", v_1_is_prime)
print("Even:", v_1_even)
print("Odd:", v_1_odd)
