
def dictionary ():
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    alter = int(input("Alter: "))
    dict = {f"{vorname}": vorname, f"{nachname}": nachname, "age": alter}
    return dict

mylist= list()

mylist.append(dictionary())
mylist.append(dictionary())
mylist.append(dictionary())


print(all([person["age"] >= 18 for person in mylist]))



