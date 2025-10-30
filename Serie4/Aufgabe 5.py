def ableitung(stammfunktion):
    dx = [stammfunktion[1]]

    [dx.append(stammfunktion[i] * i) for i in range(2, len(stammfunktion))]

    return dx


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(ableitung(mylist))
