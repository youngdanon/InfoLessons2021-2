def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


mydict = {2: 9, 5: -3, 3: 12, 7: 3, 4: 20, 1: 9, 6: 9, 11: 3, 13: 6}


def no_dup(dict):
    res_dict = {}
    no_dup_lst = list(set(dict.values()))
    v = list(dict.values())
    for i in range(len(v)):
        if v[i] in no_dup_lst:
            res_dict.update({get_key(dict, v[i]): v[i]})
    return res_dict


print(no_dup(mydict))
