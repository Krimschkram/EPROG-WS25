def rekurs(n, mylist=[0]):

    if n == 0:
        return mylist[-1]

    if len(mylist) == n+1:
        return mylist[-1]

    prev = rekurs(n-1, mylist)

    if (prev - n) > 0 and (prev - n) not in mylist:
        mylist.append(prev - n)
    else:
        mylist.append(prev + n)

    return mylist[-1]


def nicht_rekurs(n):
    mylist = [0]

    for i in range(1, n+1):
        if mylist[i-1] - i > 0 and (mylist[i-1] - i) not in mylist:
            mylist.append(mylist[i-1] - i)
        else:
            mylist.append(mylist[i-1] + i)
    return mylist[-1]



for i in range(10000):
    a = nicht_rekurs(i)
    b = rekurs(i)
    print(a == b)

    if a != b:
        print("nicht rekurs:" + str(a))
        print("rekurs:" + str(b))
        break