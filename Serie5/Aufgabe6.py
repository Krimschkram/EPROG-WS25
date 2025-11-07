def colatz_folge(n,m):
    steps = []
    steps.append(n)

    while m > 0:
        if n%2 == 0:
            n = n//2

        else:
            n = 3*n+1
        steps.append(n)
        m = m-1
        if n == 1:
            return steps, len(steps)-1
    return steps, None


print(colatz_folge(6,10))
print(colatz_folge(7,4))