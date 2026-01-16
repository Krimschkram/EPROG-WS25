import math

class Polynom:

    def __init__(self, coefficients):
        self.coefficients = coefficients  # Koeffizienten in aufsteigender Potenzordnung

    def __call__(self, x): # macht p(x) wie normale Fkt nutzbar
        return sum(coef * x**i for i, coef in enumerate(self.coefficients)) # enumerate gibt index und wert

    def degree(self):
        return len(self.coefficients) - 1

    def __add__(self, other): #addiert bzw subtrahiert stellenweise
        new_coeffs = [] #liste für neue koeffizienten
        for i in range(max(len(self.coefficients), len(other.coefficients))): # gehe bis zum größeren grad von den zwei Polynomen
            coef1 = self.coefficients[i] if i < len(self.coefficients) else 0 #Hat self Koeffizienten an Stelle i? Wenn ja, nimm den Wert, sonst 0
            coef2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs.append(coef1 + coef2)
        # schleife über alle möglichen grade und addiere koeffizienten
        # Bestimme Rückgabe-Typ basierend auf Grad
        deg = len(new_coeffs) - 1 #Grad neues Polynoms
        if deg == 1:
            return LinearFunction(new_coeffs[1], new_coeffs[0])
        elif deg == 2:
            return QuadraticFunction(new_coeffs[2], new_coeffs[1], new_coeffs[0])
        else:
            return Polynom(new_coeffs)

    def __sub__(self, other): # dasselbe wie add nur für minus
        new_coeffs = []
        for i in range(max(len(self.coefficients), len(other.coefficients))):
            coef1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coef2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coeffs.append(coef1 - coef2)
        deg = len(new_coeffs) - 1
        if deg == 1:
            return LinearFunction(new_coeffs[1], new_coeffs[0])
        elif deg == 2:
            return QuadraticFunction(new_coeffs[2], new_coeffs[1], new_coeffs[0])
        else:
            return Polynom(new_coeffs)


# Unterklasse für lineare Funktionen
class LinearFunction(Polynom):
    def __init__(self, a, b):
        super().__init__([b, a]) #ruft Basisklassen-konstruktor auf
        #[b,a], da Koeffizienten in aufsteigender Potenzordnung gespeichert werden
        # = b + a*x = [c0, c1] mit c0=b, c1=a
    def roots(self):
        a, b = self.coefficients[1], self.coefficients[0]
        if a == 0: # dann =b, konstant
            return []  # keine Nullstellen
        return [-b / a] # ax+b=0 -> x=-b/a


# Unterklasse für quadratische Funktionen
class QuadraticFunction(Polynom):
    def __init__(self, a, b, c):
        super().__init__([c, b, a])

    def roots(self):
        a, b, c = self.coefficients[2], self.coefficients[1], self.coefficients[0]
        disc = b**2 - 4*a*c #mit diskriminante
        if disc < 0:
            return []
        elif disc == 0:
            return [-b / (2*a)]
        else:
            return [(-b + disc**0.5)/(2*a), (-b - disc**0.5)/(2*a)]


# Beispielhafte Verwendung
polys = [
    LinearFunction(2, -4),
    QuadraticFunction(1, 0, -4)
]

for poly in polys:
    print(f"Polynom: {poly.coefficients}")
    print(f"Nullstellen: {poly.roots()}")