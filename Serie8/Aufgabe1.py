def sieve_of_eratosthenes(n):
    # Liste aller Prim <= n
    result = [i for i in range(2, n+1)]

    for i in result:
        print(i)
        for x in range(2, (n//2)):
            if x * i in result:
                result.remove(i * x)
    return result


print(sieve_of_eratosthenes(10))
