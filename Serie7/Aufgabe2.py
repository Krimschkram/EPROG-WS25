def sortiere_liste(liste):
    for i in range(len(liste)):
        for j in range(len(liste)):
            if liste[i] < liste[j]:
                liste[i], liste[j] = liste[j], liste[i]
    return liste


def sortiere_liste2(liste1, liste2):
    neue_liste = liste1 + liste2
    return sortiere_liste(neue_liste)

liste1 =[10,20,30,40,50]
liste2 = [55,44,33,22,11,1]

print(sortiere_liste2(liste1, liste2))
