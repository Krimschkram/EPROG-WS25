def dictionary (vorname, nachname, alter):
    dict = {f"{vorname}": vorname, f"{nachname}": nachname, "age": alter}
    return dict
test = dictionary("Marius", "Hladik", 19)
test1 = dictionary("Beni", "Newesely", 18)
test2 = dictionary("Nelia", "Passeyrer", 17)

mylist = [test,test1,test2]

if mylist[0]["age"] >= 18:
    print(mylist[0].values())
if mylist[1]["age"] >= 18:
    print(mylist[1].values())
if mylist[2]["age"] >= 18:
    print(mylist[2].values())

