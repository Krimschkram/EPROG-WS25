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



print(primes(100))