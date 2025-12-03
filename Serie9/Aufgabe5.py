def back_substitution(U, b):



    n = len(U)
    x = [0] * n

    #Input korrekt?
    if len(b) != n:
        raise ValueError("Vektor b muss die gleiche Länge wie U haben.")

    for i in range(n):
        if U[i][i] == 0:
            raise ZeroDivisionError(
                f"Null auf der Diagonale in Zeile {i}: System nicht eindeutig lösbar."
            )
    for row in U:
        if len(row) != n:
            raise ValueError("Matrix U muss quadratisch sein.")




    x[n-1] = b[n-1] / U[n-1][n-1] # Schritt 1 Angabe

    for i in range(n-2, -1, -1): # geht vom vorletzten element rückwerts bis zum 1, bsp- n = 8, dann von 6 bis 0, kann verwirrend sein

        summe = 0
        for j in range(i+1, n): # extra for loop für die Berechnugn der Summe
            summe += U[i][j] * x[j]


        x[i] = (b[i] - summe) / U[i][i] # again Formel aus der Angabe

    return x


U = [
    [2, 1, -1],
    [0, 3,  2],
    [0, 0,  4]
]

b = [2, 5, 8]

x = back_substitution(U, b)
print(x)   # erwartete Lösung
