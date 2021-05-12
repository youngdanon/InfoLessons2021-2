def merge(*args):
    result_dict = {}
    for dictt in args:
        for k, v in dictt.items():
            if k not in result_dict:
                result_dict.update({k: v})
            else:
                try:
                    result_dict.update({k: result_dict[k] + [v]})
                except:
                    buff = [result_dict[k], v]
                    result_dict.update({k: buff})

    return result_dict


print(merge({1: 2, 3: 4}, {1: 10, 2: 5, 7: 10}, {1: 7, 2: 10}))
