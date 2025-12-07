from matplotlib import pyplot as plt


def newton(f, df, x0, tol=1e-10, max_iter=100):
    """
    Standard-Newton ohne Plot (so wie in der Angabe).
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if abs(fx) < tol:
            return x
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")

        x = x - fx / dfx

    raise ValueError("Maximum iterations exceeded. No solution found.")


def newton_plot(f, df, x0, tol=1e-10, max_iter=10):
    """
    Visualisiert in jedem Schritt des Newton-Verfahrens:
    - f(x) im Intervall [x_k - 1.5*|x0 - x1|, x_k + 1.5*|x0 - x1|]
    - Tangente in x_k
    - Punkt (x_k, f(x_k))
    - Schnittpunkt x_{k+1} mit der x-Achse (roter Punkt)
    """

    # Erster Schritt, um |x0 - x1| zu bekommen
    fx0 = f(x0)
    dfx0 = df(x0)
    if dfx0 == 0:
        raise ValueError("Derivative is zero at x0. No solution found.")
    x1 = x0 - fx0 / dfx0
    step_size = abs(x1 - x0)  # |x0 - x1|

    x = x0
    for k in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if abs(fx) < tol:
            break
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")

        # Nächste Newton-Approximation
        x_next = x - fx / dfx

        # Intervall um x_k: [x_k - 1.5*|x0-x1|, x_k + 1.5*|x0-x1|]
        x_min = x - 1.5 * step_size
        x_max = x + 1.5 * step_size

        # Viele Punkte im Intervall für einen glatten Plot
        num_points = 400
        xs = [x_min + (x_max - x_min) * i / num_points for i in range(num_points + 1)]
        ys = [f(xi) for xi in xs]

        # Tangente in x_k: T(x) = f(x_k) + f'(x_k) * (x - x_k)
        tangent = [fx + dfx * (xi - x) for xi in xs]

        # Plot für diesen Schritt
        plt.figure(figsize=(8, 5))
        plt.axhline(0, color="black", linewidth=1)  # x-Achse

        plt.plot(xs, ys, label="f(x)")
        plt.plot(xs, tangent, label="Tangente in x_k")

        # aktueller Punkt (x_k, f(x_k))
        plt.scatter([x], [fx], color="green", zorder=3, label="(x_k, f(x_k))")

        # Schnittpunkt der Tangente mit x-Achse (x_{k+1}, 0)
        plt.scatter([x_next], [0], color="red", zorder=4, label="x_{k+1}")

        plt.title(f"Newton-Verfahren, Schritt {k}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        x = x_next  # zum nächsten Schritt

    return x

def f(x):
    return x**2 - 2

def df(x):
    return 2*x

wurzel = newton_plot(f, df, x0=1.0)
print("Approximierte Wurzel:", wurzel)
