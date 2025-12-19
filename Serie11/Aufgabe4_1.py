import numpy as np

a = np.array([1, 2, 3, 4, 5])

b = a.view()   # VIEW: teilt sich die Daten mit a
c = a.copy()   # COPY: eigene Daten

# Änderungen durchführen
b[0] = 100
c[1] = 200

print("a:", a)
print("b (view):", b)
print("c (copy):", c)
