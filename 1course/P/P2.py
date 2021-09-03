def f19(m_num):
    m_dict = {1: 'Январь',
              2: 'Февраль',
              3: 'Март',
              4: 'Апрель',
              5: 'Май',
              6: 'Июнь',
              7: 'Июль',
              8: 'Август',
              9: 'Сентябрь',
              10: 'Октябрь',
              11: 'Ноябрь',
              12: 'Декабрь'}
    return m_dict[m_num]


def f20(m_num):
    pora_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
    for pora in pora_dict:
        if m_num in pora_dict[pora]:
            return pora


def f21(num):
    dict = {}
    for i in range(1, num):
        dict.update({i: i * i * i})
    return dict


def f21_1(dict):
    res = 1
    for _, v in dict.items():
        res *= v
    return res


def f22(lst1, lst2):
    dict = {}
    for i in range(len(lst1)):
        dict.update({lst1[i]: lst2[i]})
    return dict


def f23(dic: dict):
    res_dic = {}
    for k, v in dic.items():
        res_dic.update({v: k})
    return res_dic


def f24(list1, list2):
    return list(set(list1) & set(list2))


def f25(dic: dict, k, v):
    if k in dic.keys():
        a = [dic[k], v]
        dic[k] = a
    else:
        dic.update({k: v})
    return dic


def f26(str):
    res_dic = {}
    for sym in str:
        res_dic.update({sym: str.count(sym)})
    return res_dic


lst1 = [1, 2, 3, 4, 5]
lst2 = ['a', 'b', 'c', 'd', 'e']
lst3 = [2, 5, 7, 10, 1]
dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
dict1 = {1: "a", 2: "b", 3: "c"}

print('f19 : ', f19(1))
print('f20 : ', f20(3))
print('f21 : ', f21(10))
print('f21_1 : ', f21_1(dict))
print('f22 : ', f22(lst1, lst2))
print('f23 : ', f23(dict1))
print('f24 : ', f24(lst1, lst3))
print('f25 : ', f25(dict1, 3, 123))
print('f26 : ', f26("queue"))
