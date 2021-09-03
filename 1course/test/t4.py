mystr = "Привееет! Как Дела?"


def salt_lang(string):
    res_str = ""
    glas_lst = ["А", "Е", "Ё", "И", "О", "У", "Э", "Ю", "Я", "а", "е", "ё", "и", "о", "у", "э", "ю", "я"]
    for i in range(len(string)):
        if string[i] in glas_lst:
            res_str += string[i] + "c" + string[i]
        else:
            res_str += string[i]
    return res_str


print(salt_lang(mystr))

