import math

class polynom:
    """
    Ein Polynom f(x) = a0 + a1*x + ... + an*x^n
    Die Koeffizienten werden als Liste [a0, ..., an] übergeben.
    """

    def __init__(self, coeffs):
        # coeffs[i] = Koeffizient vor x^i
        self.coeffs = list(coeffs)
        self.degree = len(self.coeffs) - 1

    # 1. Auswertung an einer Stelle x
    def eval(self, x):
        """Berechnet f(x) für ein gegebenes x."""
        value = 0
        for power, coefficient in enumerate(self.coeffs):
            value += coefficient * (x ** power)
        return value

    # 2. Ableitung
    def diff(self):
        """Gibt das Ableitungspolynom f'(x) als neues polynom-Objekt zurück."""
        if self.degree == 0:
            # Ableitung einer Konstante ist 0
            return polynom([0])

        derived_coeffs = []
        for power, coefficient in enumerate(self.coeffs):
            if power == 0:
                continue  # Konstante fällt weg
            derived_coeffs.append(power * coefficient)

        return polynom(derived_coeffs)

    # 3. Bestimmtes Integral von x1 bis x2
    def integrate(self, x1, x2):
        """
        Berechnet ∫_{x1}^{x2} f(x) dx über die Stammfunktion
        F(x) = a0*x + a1*x^2/2 + ... + an*x^{n+1}/(n+1)
        und gibt F(x2) - F(x1) zurück.
        """
        def primitive(x):
            value = 0
            for power, coefficient in enumerate(self.coeffs):
                new_power = power + 1
                value += coefficient * (x ** new_power) / new_power
            return value

        return primitive(x2) - primitive(x1)

    # 4. Nullstellen (nur bis Grad 2)
    def zeros(self):
        """
        Berechnet die Nullstellen, falls das Polynom höchstens Grad 2 hat.
        - Grad > 2: ValueError
        - Keine reellen Nullstellen: None
        - Sonst: eine Zahl oder Tupel (x1, x2)
        """
        if self.degree > 2:
            raise ValueError("Nullstellen nur für Polynome bis Grad 2 implementiert.")

        # Grad 0: f(x) = a0
        if self.degree == 0:
            a0 = self.coeffs[0]
            if a0 == 0:
                # unendlich viele Nullstellen; hier vereinfachend:
                return None
            else:
                return None  # konstante ungleich 0 → keine Nullstellen

        # Grad 1: f(x) = a0 + a1*x
        if self.degree == 1:
            a0, a1 = self.coeffs
            if a1 == 0:  # eigentlich schon in Grad 0 aufgefangen
                return None
            x = -a0 / a1
            return x

        # Grad 2: f(x) = a0 + a1*x + a2*x^2
        a0, a1, a2 = self.coeffs
        if a2 == 0:
            # eigentlich nur ein lineares Polynom – zur Sicherheit:
            if a1 == 0:
                return None
            return -a0 / a1

        diskriminante = a1**2 - 4*a2*a0

        if diskriminante < 0:
            # keine reellen Nullstellen
            return None
        elif diskriminante == 0:
            x = -a1 / (2 * a2)
            return x
        else:
            wurzel_D = math.sqrt(diskriminante)
            x1 = (-a1 + wurzel_D) / (2 * a2)
            x2 = (-a1 - wurzel_D) / (2 * a2)
            return (x1, x2)

    # 5. statische Methode: Summe zweier Polynome
    @staticmethod
    def add(p1, p2):
        """
        Addiert zwei Polynome und gibt ein neues polynom-Objekt zurück.
        """
        max_len = max(len(p1.coeffs), len(p2.coeffs))
        # Koeffizientenlisten auf gleiche Länge auffüllen
        c1 = p1.coeffs + [0] * (max_len - len(p1.coeffs))
        c2 = p2.coeffs + [0] * (max_len - len(p2.coeffs))

        sum_coeffs = [c1[i] + c2[i] for i in range(max_len)]
        return polynom(sum_coeffs)


# ------------------ Tests / Beispiele ------------------

if __name__ == "__main__":
    # f(x) = 1 + 2x + 3x^2
    f = polynom([1, 2, 3])

    print("f(2) =", f.eval(2))                 # Auswertung
    f_prime = f.diff()
    print("f'(x) Koeffizienten:", f_prime.coeffs)

    # Integral von 0 bis 1
    print("∫_0^1 f(x) dx =", f.integrate(0, 1))

    # Nullstellen eines quadratischen Polynoms: g(x) = -1 + 0x + 1x^2 = x^2 - 1
    g = polynom([-1, 0, 1])
    print("Nullstellen von g:", g.zeros())

    # Summe zweier Polynome
    h = polynom([0, 1])        # h(x) = x
    s = polynom.add(f, h)      # f(x) + h(x)
    print("f(x) + h(x) Koeffizienten:", s.coeffs)
