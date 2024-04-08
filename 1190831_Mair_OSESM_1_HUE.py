
import numpy as np
import random

v_1 = 100
v_2 = 20

# Überschreibung von Variablen
v_1 = v_2

# Ausgabe einer Variable
print("Wert von Variable 1:",v_1)
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

Summe = v_1 + v_2
Produkt = v_1 * v_1
Sub = v_1 - v_1
Div = v_1 / v_1
Pot = v_1 ** v_1

print("Summe:",Summe)
print("Produkt:",Produkt)
print("Sub:",Sub)
print("Div:",Div)
print("Pot:",Pot)