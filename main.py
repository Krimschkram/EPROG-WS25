def rek_list(L):
    resul = []
    for element in L:
        if type(element) == int:
            return element
        if type(element) == list:
            resul.append(rek_list(element))





my_list = [1,2,3,4,5, [10,11, 12, [13, 14]], 20, 30]