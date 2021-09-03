mydict = {2: 9, 5: -3, 3: 12, 7: 3, 4: 20, 1: 9, 6: 9, 11: 3, 13: 6}

n = int(input())


def fill(dict_func, m):
    res_dict = {}
    for i in range(m):
        if i not in dict_func:
            res_dict.update({i: "!!"})
        else:
            res_dict.update({i: dict_func.get(i)})
    return res_dict


print(fill(mydict, n))
