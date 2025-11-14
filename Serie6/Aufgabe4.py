def mymap(func, iterable):
    result = []
    for x in iterable:
        result.append(func(x))
    return result


def myfilter(func, iterable):
    result = []
    for x in iterable:
        if func(x):
            result.append(x)
    return result

def myreduce(func, iterable):
    if len(iterable) == 0:
        raise TypeError("leer")

    result = iterable[0]

    for x in iterable[1:]:
        result = func(result, x)
    return result


# mymap
print(mymap(lambda x: x * 2, [1, 2, 3]))        # [2, 4, 6]
print(mymap(str.upper, ["hi", "test"]))         # ["HI", "TEST"]

# myfilter
print(myfilter(lambda x: x % 2 == 0, [1, 2, 3, 4]))   # [2, 4]
print(myfilter(lambda w: len(w) > 3, ["hi", "auto", "ok", "test"]))
# ["auto", "test"]

# myreduce2
print(myreduce(lambda a, b: a + b, [1, 2, 3, 4]))    # 10
print(myreduce(lambda a, b: a + b, ["Py", "thon"]))  # "Python"
