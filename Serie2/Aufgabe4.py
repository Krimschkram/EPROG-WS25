# Aufgabe 4
import math

n = int(input("Wie viele Personen befinden sich in deiner Gruppe?"))

P = 1 - (math.factorial(365))/(365**n * math.factorial(365 - n))
# gewöhnliche rechnung laut angabe
# aufgepasst bei math.paw und **, führt beides die gleiche Rechnung durch also "x hoch y"
# math.paw verwendet float als Daten typ, ** nicht, deshalb eignet sich ** besser

print(f"Die Wahrscheinlichkeit, dass jemand deinen Geburtstag teilt, liegt bei {P*100:.2f}%")



# Bonus:
i = 1
# i ist ein counter der immer um 1 erhöt wird

# While True = Endlosschleife (muss manuell abgebrochen werden bsp. break/return
while True:
    P = 1 - (math.factorial(365)) / (365 ** i * math.factorial(365 - i))
    #fügt i in unsere Formel aus der Angabe ein

    # sind wir über %, wenn ja print und schleife abbrechen, ansonsten weitermachen
    if P*100>= 50:

        print("Bei einer Personanzahl ab" , i , "übersteigt die Wahrscheinlichkeit 50%, dass sich ein Geburtstag überschneidet")
        break
    # i erhöhen
    i+=1