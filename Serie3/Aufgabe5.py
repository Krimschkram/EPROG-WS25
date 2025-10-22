# Aufgabe 5

def loesche_werte(liste, wert):
    while wert in liste:   # solange der Wert noch in der Liste ist
        liste.remove(wert) # entferne das erste Vorkommen

liste = [1, 2, 3, 2, 2, 4, 5]
loesche_werte(liste, 2)
print(liste)
