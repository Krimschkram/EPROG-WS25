# Aufgabe 4
import random

# zugegebenermaßen eine komische Variante Schere Stein Papier zu spielen so ist aber aus der Angabe verlangt so wie ich verstehe

def schere_stein_papier(throw_user):
    # kopierter code aus dem Sktipt
    # Vorgenommene Änderun: Code wurde in eine Funktion geschrieben, lässt sich dann auch in anderen Funktionen aufrufen
    # Je nach dem ob der User oder Computer gewinnt wird ein -1 oder +1 zurückgegeben.
    # cheat Funktion habe ich ebenfalls entfernt (ist zum Testen einfacher)
    throw_computer = random.randint(1, 3)

    # Check result
    if throw_computer == throw_user:
        print("Unentschieden")
    elif throw_computer == 1 and throw_user == 2:
        print("Stein bricht Schere, du gewinnst!")
        return 1
    elif throw_computer == 1 and throw_user == 3:
        print("Schere schneidet Papier, Computer gewinnt!")
        return -1
    elif throw_computer == 2 and throw_user == 1:
        print("Stein bricht Schere, Computer gewinnt!")
        return -1
    elif throw_computer == 2 and throw_user == 3:
        print("Papier bedeckt Stein, du gewinnst!")
        return 1
    elif throw_computer == 3 and throw_user == 1:
        print("Schere schneidet Papier, du gewinnst!")
        return 1
    elif throw_computer == 3 and throw_user == 2:
        print("Papier bedeckt Stein, Computer gewinnt!")
        return -1
    else:
        print("Ungültige Eingabe")


def starte_schere_stein_papier():
    # mit der Funktion spiele ich 3 mal hintereinander
    siege_computer = 0
    siege_user = 0

    for i in range(3):
        # range(3) liefert 0,1,2, geht also drei mal durch die For Schleife durch
        print(f"Der Zwischenstand liegt: Computer {siege_computer}, Du: {siege_user}")

        throw_user = int(input("Schere(1), Stein(2), Papier(3): "))

        ergebnis = schere_stein_papier(throw_user)
        # ergebnis beträgt je nach Sieger 1 oder -1
        # wenn du nicht weißt, was das heißt werfe einen Blick in die Funktion "schere_stein_papier"

        if ergebnis == 1:
            siege_user += 1

        if ergebnis == -1:
            siege_computer += 1
    print(f"Endstand: Computer - {siege_computer}, Du - {siege_user}")
    if siege_computer == siege_user:
        print("Unentschieden")
        return
    if siege_computer > siege_user:
        print("Computer gewinnt!")
        return
    print("Du gewinnst!")

    if siege_user > siege_computer:
        print("Gratulation du hast gewonnen!")
        return
    print("Vielleicht nächstes mal, der Computer hat dich besiegt...")


starte_schere_stein_papier()
# so lässt sich das Spiel aufrufen
# Was passiert? "starte_schere_stein_papier" rufen wir auf, und diese Funktion ruft dann unsere zweite Funktion auf, so arbeiten sie zusammen