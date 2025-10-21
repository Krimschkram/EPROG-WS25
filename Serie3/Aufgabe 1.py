# Aufgabe 1

n1 = int(input("n_1 = "))
n2 = int(input("n_2 = "))



# % liefert den Rest einer Dividion, and verknüpft bedingungen

if n1 > n2 and n1%n2 == 0:
    print(f"Die Zahl {n1} lässt sich ohne Restbetrag durch {n2} dividieren")
if n2 > n1 and n2%n1 == 0:
    print(f"Die Zahl {n2} lässt sich ohne Restbetrag durch {n1} dividieren")

    