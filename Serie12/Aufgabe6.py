import numpy as np
import matplotlib.pyplot as plt


# Monte-Carlo-Approximation eines Integrals

def mc_integral(funktion, a, b, anzahl_punkte):
    x = np.random.uniform(a, b, anzahl_punkte)
    return (b - a) * np.mean(funktion(x))


def funktion(x):
    return x**2

a = 0.0
b = 1.0
exakter_wert = 1.0 / 3.0


n_werte = [50, 100, 200, 400, 800, 1600, 3200, 6400, 12800]
anzahl_wiederholungen = 50

mittlere_fehler = []

for n in n_werte:
    fehler = []
    for _ in range(anzahl_wiederholungen):
        approximation = mc_integral(funktion, a, b, n)
        fehler.append(abs(approximation - exakter_wert))
    mittlere_fehler.append(np.mean(fehler))

mittlere_fehler = np.array(mittlere_fehler)
n_werte = np.array(n_werte)




plt.figure()
plt.loglog(n_werte, mittlere_fehler, marker="o", label="mittlerer Fehler")

# Referenzlinie ~ 1/sqrt(n)
referenz = mittlere_fehler[0] * np.sqrt(n_werte[0] / n_werte)
plt.loglog(n_werte, referenz, linestyle="--", label=r"$\sim 1/\sqrt{n}$")

plt.xlabel("Anzahl der Zufallspunkte n")
plt.ylabel("mittlerer Fehler")
plt.title("Monte-Carlo-Integration: Fehler in Abhängigkeit von n")
plt.legend()
plt.show()
