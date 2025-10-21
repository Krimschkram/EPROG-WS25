# Aufgabe 2


# Ich bin mir nicht sicher, ob das mit dem unregelmäßiges überhaupt gefragt ist, Angabe bissl komisch formuliert

def triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        # gibt einen String zurück, den ich dann ausgeben kann, könnte ich aber auch weiterverwenden wichtig für den Aufruf der Funktion
        return "Ungültiges Dreieck"

    if a == b and a == c:
        return "Gleichseitiges Dreieck"

    if a == b or a == c or b == c:
        return "Gleichschenkeliges Dreieck"

    if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        return "Rechtwinkeliges Dreieck"

    return "Unregelmäßiges Dreieck"


a = int(input("Seitenlänge a = "))
b = int(input("Seitenlänge b = "))
c = int(input("Seitenlänge c = "))

s = triangle(a, b, c)
# hier lässt sich unser ergebnis zwischenspeichern, ist praktisch sollten wir das mal später wieder brauchen
print("Dein Dreieck ist ein",s)
