from math import floor
def null(x):
    n=len(x)
    #x.sort
    r=n-1
    l=0
    while l<=r:
        m=(l+r)//2
        if x[m] == 0:
            return True
        elif x[m]>0:
            r=m-1
        else:
            l=m+1
    return False
v=[0, 1, 2, 2, 3, 4, 5]
print(null(v))


from math import floor
def irgendwas(x, y):
    n=len(x)
    #x.sort
    r=n-1
    l=0
    while l<=r:
        m=(l+r)//2
        if x[m] == y:
            return True
        elif x[m]>y:
            r=m-1
        else:
            l=m+1
    return False
v=[0, 1, 2, 2, 3, 4, 5]
print(null(v))