import math
import random

# Aufgabe 1
print(10* "-","Aufgabe 1", "-" * 10)
name = input("Wie lautet dein Name?")
age = input("Wie alt bist du?")


print("Hallo ich heiße", name, "und bin", age, "Jahre alt")



# Aufgabe 2
print(10* "-","Aufgabe 2", "-" * 10)

print("Geben Sie zwei Natürliche Zahlen an")
n1 = int(input("n1 = "))
n2 = int(input("n2 = "))

print("Divisionsrest von ",n1,"/",n2,"=",n1%n2)
print()

# Aufgabe 3
print(10* "-","Aufgabe 3", "-" * 10)

pi = math.pi

approximationen = [3, 3.14, 22/7, 355/113]

print(f"{'Approximation':>15} | {'Relativer Fehler':>15} | {'Prozent':>8}")
print("-" * 48)

for x in approximationen:
    rel_fehler = abs(pi - x) / pi
    prozent = rel_fehler * 100
    print(f"{x:15.6f} | {rel_fehler:16.6f} | {prozent:8.2f}%")


# Aufgabe 4
print(10* "-","Aufgabe 4", "-" * 10)

n = int(input("Wie viele Personen befinden sich in deiner Gruppe?"))

P = 1 - (math.factorial(365))/(365**n * math.factorial(365 - n))

print(f"Die Wahrscheinlichkeit, dass jemand deinen Geburtstag teilt, liegt bei {P*100:.2f}%")

# Bonus:
i = 0
while True:
    P = 1 - (math.factorial(365)) / (365 ** i * math.factorial(365 - i))

    if P*100>= 50:

        print("Bei einer Personanzahl ab" , i , "übersteigt die Wahrscheinlichkeit 50%, dass sich ein Geburtstag überschneidet")
        break
    i+=1


# Aufgabe 5
print(10* "-","Aufgabe 5", "-" * 10)

n1 = int(input("Zahl1 ="))
n2 = int(input("Zahl2 ="))
print("Die größere Zahl lautet", max(n1,n2))


# Aufgabe 6
print(10* "-","Aufgabe 6", "-" * 10)

wuerfel1 = random.randint(1,6)
wuerfel2 = random.randint(1,6)

print(f"({wuerfel1},{wuerfel2}) =",wuerfel1 + wuerfel2)