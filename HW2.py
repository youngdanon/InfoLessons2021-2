from itertools import zip_longest as zl


def f1(arr, a=0, b=None):
    if b is None:
        b = len(arr) - 1
    return sum(arr[a:b + 1])


def f2_first(arr, remove_obj):
    while remove_obj in arr:
        arr.remove(remove_obj)
    return arr


def f2_second(arr, remove_obj):
    new_arr = [i for i in arr if i != remove_obj]
    return new_arr


def f3(arr, a, b):
    return arr[:a] + arr[b:(a - 1):-1] + arr[b + 1:]


def f4(arr, steps):
    steps = -steps
    return arr[steps:] + arr[:steps]


def f5(*args):
    new_arr = []
    for arr in args:
        new_arr += arr
    return new_arr


def f6(arr_1, arr_2):
    len_1, len_2 = len(arr_1), len(arr_2)
    new_arr = []
    if len_1 < len_2:
        for i in range(len_1):
            new_arr += [arr_1[i], arr_2[i]]
        new_arr += arr_2[len_1:]
    else:
        for i in range(len_2):
            new_arr += [arr_1[i], arr_2[i]]
        new_arr += arr_1[len_2:]
    return new_arr


def f7(arr1, arr2):
    zipped = list(zl(arr1, arr2))
    res_lst = []
    for i in zipped:
        for j in i:
            if j is not None:
                res_lst.append(j)
    return res_lst


def f8(arr):
    res_lst = []
    for i in range(len(arr) - 1):
        res_lst.append((arr[i], arr[i + 1]))
    return res_lst


def f1_1(arr, a=0, b=None):
    if b is None:
        b = len(arr) - 1
    sliced = arr[a: b + 1]
    res = 1
    for i in sliced:
        res *= i
    return res


def f1_2(arr):
    return f1(arr[::2]), f1_1(arr[1::2])


def f1_3(arr):
    even_arr, odd_arr = [], []
    for i in arr:
        if i % 2 == 0:
            even_arr.append(i)
        else:
            odd_arr.append(i)
    return f1(even_arr), f1_1(odd_arr)


a = [4, 6, 8, 1, -9, 0, 1, 2, 1, 7]

print("f1", f1(a, 2, 4))
print("f2_first", f2_first(a, 1))
print("f2_second", f2_second(a, 1))
print("f3", f3(a, 2, 5))
print("f4 ", f4(a, 2))
l_1 = [1, 2, 3]
l_2 = [4, 5]
l_3 = [6]
print("f5 ", f5(l_1, l_2, l_3))
print("f6 ", f6([1, 1, 1, 1], [0, 0, 0]))
print("f7 ", f7([1, 1, 1, 1], [0, 0, 0]))
print("f8 ", f8([1, 2, 3, 4, 5, 6]))
print("f1_1", f1_1(a, 2, 4))
print("f1_2", f1_2([2, 2, 2, 3]))
print("f1_3", f1_3([2, 2, 2, 3]))
