def quersumme(x):
    s = str(x)
    erg = 0
    for char in s:
        erg+= int(char)
    return erg


print(quersumme(1034))



M = [[0 for x in range(3)] for y in range(3)]

print(M)