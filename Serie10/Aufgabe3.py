from matplotlib import pyplot as plt


def newton(f, df, x0, tol=1e-10, max_iter=100):
    """
    f : function
        The function for which we want to find a root.
    df : function
        The derivative of the function f.
    x0 : float
        The initial guess for the root.
    tol : float
        The tolerance for convergence.
    max_iter : int
        The maximum number of iterations.

    Returns:
    float
        The estimated root of the function f.
    """
    x = x0
    x1 = x0 - f(x0)/df(x0)

    def plot_newton(xk):
        xk_next = xk - f(xk) / df(xk)

        a = (xk - 1.5 * abs(x0 - x1))
        b = xk + 1.5 * abs(x0 - x1)

        x_plot = [a + (b - a) * i / 200 for i in range(200 + 1)] # Auf so eine Erklärung vorbereiten
        y_plot = [f(xi) for xi in x_plot]
        plt.plot(x_plot, y_plot)
        plt.xlabel("x")
        plt.ylabel("P(x)")

        y_plot2 = [j * 0 for j in range(200 + 1)]
        plt.plot(x_plot, y_plot2)


        k = df(xk) # Steigung
        d = f(xk) - k * xk # Ordinatenabschnitt
        def apporx(z):
            return k * z + d


        plt.scatter(xk, f(xk), color="red", label="schnittpunkt")
        plt.scatter(xk_next, 0, color="green", label="nullstelle")
        plt.legend()
        y_plot = [apporx(xi) for xi in x_plot]
        plt.plot(x_plot, y_plot)


        plt.title('Brr Brr patapim')
        plt.xlabel('x')
        plt.ylabel('y')


        plt.show()


    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x -= fx / dfx
        plot_newton(x)
    raise ValueError("Maximum iterations exceeded. No solution found.")


def test(x):
    return x ** 2
def testd(x):
    return 2*x

newton(test, testd, 1)