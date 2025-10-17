import math
# Aufgabe 3

pi = math.pi

approximationen = [3, 3.14, 22/7, 355/113]
# Liste aller Näherungen von Pi mit approximationen[0-3] lassen sie sich ausgeben

print(f"{'Approximation':>15} | {'Relativer Fehler':>15} | {'Prozent':>8}")
print("-" * 48)

# generiert ein Table head, lässt sich durch ein wenig herumspielen generieren

for x in approximationen: # 4 durchläufe, in jeden durchlauf, wechselt der Zustand von x auf das nächste element von approximationen
    rel_fehler = abs(pi - x) / pi # Berechnung laut angabe

    prozent = rel_fehler * 100 # zwischen variable
    print(f"{x:15.6f} | {rel_fehler:16.6f} | {prozent:8.2f}%") # gibt in einem ähnlichen Format, wie der table head unsere werte aus

