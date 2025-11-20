def initialisiere_staebe(n):
    """
    Erzeuge die Anfangsanordnung für n Scheiben:
    alle Scheiben liegen auf Stab 1, 1 ist die kleinste Scheibe.
    """
    # größte unten (n) bis kleinste oben (1), oberste = letztes Element
    return [list(range(n, 0, -1)), [], []]

def bewege_scheibe(staebe, von, nach):
    """
    Bewegt die oberste Scheibe von Stab 'von' zu Stab 'nach'.
    von und nach sind hier 1,2,3 (nicht 0,1,2), damit der Output schön ist.
    """
    scheibe = staebe[von - 1].pop()      # oberste Scheibe von Stab 'von'
    staebe[nach - 1].append(scheibe)     # auf Stab 'nach' legen
    print(f"Bewege Scheibe von Stab {von} zu Stab {nach}")

def hanoi(n, erster_stab, zweiter_stab, dritter_stab, staebe):
    """
    Rekursiver Algorithmus:
    bewegt n Scheiben von Stab 'von' nach Stab 'nach'
    unter Verwendung des Hilfsstabs 'hilfs'.
    """
    if n == 0:
        # nichts zu tun
        return
    print(staebe)
    # 1. n-1 Scheiben auf den Hilfsstab verschieben
    hanoi(n - 1, erster_stab, dritter_stab, zweiter_stab, staebe)

    # 2. größte (unterste) Scheibe von 'von' nach 'nach'
    bewege_scheibe(staebe, erster_stab, zweiter_stab)

    # 3. n-1 Scheiben vom Hilfsstab auf den Zielstab verschieben
    hanoi(n - 1, dritter_stab, zweiter_stab, erster_stab, staebe)


def loese_hanoi(n):
    """
    Hilfsfunktion: bereitet die Stäbe vor und löst das Problem
    für n Scheiben von Stab 1 nach Stab 3.
    Gibt am Ende die Stab-Konfiguration zurück.
    """
    staebe = initialisiere_staebe(n)
    hanoi(n, 1, 3, 2, staebe)
    return staebe


print(loese_hanoi(3))