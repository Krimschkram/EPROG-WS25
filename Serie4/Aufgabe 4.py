import math

psi = (1 + math.sqrt(5)) / 2

# in formel einsetzen
formel = [round((psi**n - (-psi)**(-n)) / math.sqrt(5)) for n in range(1, 21)]

print(formel)


# Startwerte
psi = [1, 1]

# rekursiv, das letzte Element 6 dem vorletzten
[psi.append(psi[-1] + psi[-2]) for _ in range(18)]

print(psi)
