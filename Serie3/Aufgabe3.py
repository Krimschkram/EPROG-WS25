import math


def mittelwert_standartabweichung(n1, n2, n3):
    mittelwert = (n1 + n2 + n3) / 3

    # aufpassen laute der Angabe müssen wir die Stichproben Standartabweichung berechnen, nicht die Standartabweichugn der Grundgesamtheit
    standartabweichung = ((n1 - mittelwert)**2 + (n2 - mittelwert)**2 + (n3 - mittelwert)**2) / 2

    # Die Wurzel weil angabe: s^2 = ....
    return f"Mittelwert: {mittelwert}, Standartabweichung: {math.sqrt(standartabweichung)}"

print(mittelwert_standartabweichung(52,93,15))
print(mittelwert_standartabweichung(72,61,21))
print(mittelwert_standartabweichung(83,87,75))