def newton(f, fprime, x0, tol):
    x_prev = None
    x = float(x0)

    while True:
        fx = f(x)
        fpx = fprime(x)
        if abs(fx) < tol:
            return x # Nullstelle gefudnen
        if abs(fpx) <= tol*abs(fx):
            raise RuntimeError(f"Function {x} did not converge")

        x_new = x -fx/fpx # Formel aus Anfgabe

        if x_prev is None and abs(x_new-x) < tol:
            return x_new # Nullstelle gefunden
        x_prev = x
        x = x_new
