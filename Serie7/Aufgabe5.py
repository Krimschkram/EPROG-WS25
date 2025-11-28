def diff(f,h0,eps, x):
    def phi(h):
        return (f(x+h) - f(x))/h
        # (f(x + h) - 2*f(x) + f(x - h)) / (h*h)

    def rek(h):
        phi_h = phi(h)
        phi_h2 = phi(h / 2)

        # Abbruchbedingung der Aufgabe:
        if abs(phi_h - phi_h2) <= eps * abs(phi_h):
            return phi_h2, h / 2

        # sonst weiter halbieren
        return rek(h / 2)   
    return rek(h0)


def f1(x):
    return x**2
h0_1 = 0.1
eps_1 = 1e-6
print(diff(f1, h0_1, eps_1, 0))


