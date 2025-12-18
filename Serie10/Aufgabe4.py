from matplotlib import pyplot as plt

# gegebene Funktion und Ableitung
def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1


def bisection_sequence(f, a, b, tol=1e-10, max_iter=50):
    """Liefert die Folge der Bisektions-Mittenpunkte x_i."""
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) und f(b) müssen unterschiedliches Vorzeichen haben.")

    xs = []
    for _ in range(max_iter):
        m = 0.5 * (a + b)
        xs.append(m)

        if abs(f(m)) < tol:
            break

        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return xs


def newton_sequence(f, df, x0, tol=1e-10, max_iter=50):
    """Liefert die Folge der Newton-Iterate x_i."""
    xs = [x0]
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if abs(fx) < tol:
            break
        if dfx == 0:
            raise ValueError("Ableitung ist 0, Newton bricht ab.")

        x = x - fx / dfx
        xs.append(x)
    return xs

# Folge der Approximationen für f(x) = x^3 - x - 2
bis_xs = bisection_sequence(f, 1, 3)
new_xs = newton_sequence(f, df, 2)   # Startwert x0 = 2

# Fehlerwerte |f(x_i)|
bis_errs = [abs(f(x)) for x in bis_xs]
new_errs = [abs(f(x)) for x in new_xs]

bis_it = list(range(len(bis_xs)))
new_it = list(range(len(new_xs)))

# --- Plot 1: normale y-Achse ---
plt.figure(figsize=(7, 5))
plt.plot(bis_it, bis_errs, "o-", label="Bisektionsverfahren")
plt.plot(new_it, new_errs, "s-", label="Newton-Verfahren")

plt.xlabel("Iteration i")
plt.ylabel(r"$|f(x_i)|$")
plt.title(r"Konvergenzvergleich: $f(x)=x^3 - x - 2$")
plt.legend()
plt.grid(True, linestyle=":")
plt.tight_layout()

# --- Plot 2: logarithmische y-Achse ---
plt.figure(figsize=(7, 5))
plt.plot(bis_it, bis_errs, "o-", label="Bisektionsverfahren")
plt.plot(new_it, new_errs, "s-", label="Newton-Verfahren")

plt.xlabel("Iteration i")
plt.ylabel(r"$|f(x_i)|$ (log-Skala)")
plt.yscale("log")             # <--- log-Skalierung
plt.title(r"Konvergenzvergleich (log-Skala): $f(x)=x^3 - x - 2$")
plt.legend()
plt.grid(True, which="both", linestyle=":")
plt.tight_layout()

plt.show()
