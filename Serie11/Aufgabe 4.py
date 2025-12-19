import numpy as np


def list_to_numpy(lst):
    brr = np.array(lst)


    copy = brr.copy()
    view = brr.view()

    copy = 0
    view = 0
    print("Array:")
    print(brr)
    print("Shape (Dimensionen):", brr.shape)
    print("Anzahl der Dimensionen (ndim):", brr.ndim)
    print()

    return brr


list_1d = [1, 2, 3, 4, 5]
arr_1d = list_to_numpy(list_1d)

list_2d = [[1, 2, 3], [4, 5, 6]]
arr_2d = list_to_numpy(list_2d)

list_3d = [[[1, 2],[3, 4]],[[5, 6],[7, 8]]]
arr_3d = list_to_numpy(list_3d)

print(arr_3d)

