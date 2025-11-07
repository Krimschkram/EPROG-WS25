def is_prim(n):
    isPrim = True
    for i in range(2,n):
        if n%i==0:
            isPrim = False
    return isPrim

def primes(n):
    primes_list = []
    for i in range(2,n):
        if is_prim(i):
            primes_list.append(i)
    return primes_list

def pfz(n):
    faktorzerlegung = {}
    for p in primes(n+1):  # alle Primzahlen bis n
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        if exponent > 0:
            faktorzerlegung[p] = exponent
        if n == 1:
            break
    return faktorzerlegung


print(pfz(15))



