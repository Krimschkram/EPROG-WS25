import time


import time

def pruefe_alter(alter, geburtsjahr):
    sekunden_pro_jahr = 365 * 24 * 60 * 60
    aktuelles_jahr = 1970 + time.time() / sekunden_pro_jahr
    # time.time liefert die vergangenen sekunden deswegen der Aufwand 1.1.1970
    berechnetes_alter = int(aktuelles_jahr) - geburtsjahr

    # Wenn Alter und berechnetes Alter übereinstimmen → True, sonst False
    if berechnetes_alter == alter:
        return True
    else:
        return False


# Beispiele:
print(pruefe_alter(25, 2000))
print(pruefe_alter(30, 1995))
print(pruefe_alter(50, 1980))



