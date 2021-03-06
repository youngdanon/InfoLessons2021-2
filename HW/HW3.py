from matplotlib import pyplot as plt
from math import sqrt

buff_dict = {}
buff_list = []
residents_buff_dict = {}
residents_buff_list = []
first_market = ()
residents_first_market = ()


def dict_sorting_by_values(dict):
    return {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}


def distance(x1, y1, x2, y2):
    dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dist


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def check_buildings_amount(db: dict, rad):
    buildings_amount_dict = {}
    for elem1 in db.values():
        buildings_amount = 0
        for elem2 in db.values():
            if elem1 != elem2:
                if distance(float(elem1[0]), float(elem1[1]), float(elem2[0]), float(elem2[1])) <= rad:
                    buildings_amount += 1
        buildings_amount_dict.update({get_key(db, elem1): buildings_amount})
    return dict_sorting_by_values(buildings_amount_dict)


def check_residents_amount(db, rad):
    residents_amount_dict = {}
    for elem1 in db.values():
        residents_amount = 0
        for elem2 in db.values():
            if elem1 != elem2:
                if distance(float(elem1[0]), float(elem1[1]), float(elem2[0]), float(elem2[1])) <= rad:
                    residents_amount += elem2[2] * 0.7 / 18
        residents_amount_dict.update({get_key(db, elem1): residents_amount})
    return dict_sorting_by_values(residents_amount_dict)


def read_data(path):
    """
    Чтение файла и сохранение в словаре вида: ключ адрес, значения это кортеж (координата Х, коордианата Y, площадь)
    Пример: {'пр-кт Фатыха Амирхана д 91Б': (5.73063, 11.8712, 2095.0), ... }
    Args:
        path (str): путь к файлу
    Returns:
        dict: ключ адрес, значение (x, y, площадь)
    """
    database = {}
    with open("./buildings", encoding="utf-8") as file:
        for line in file:
            raw_row = line.split("\t")
            database.update({raw_row[0]: tuple(map(float, raw_row[1:4]))})
    return database


def task1(db):
    global buff_dict
    global first_market
    global buff_list
    global residents_buff_dict
    global residents_buff_list
    global residents_first_market
    """
    Задача 1
    Args:
        db (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
        помимо database могут быть любые другие аргументы
    Returns:
        list: координаты дома (x, y)
    """
    buff_dict = check_buildings_amount(db, 0.5)
    buff_list = list(buff_dict)
    residents_buff_dict = check_residents_amount(db, 0.5)
    residents_buff_list = list(residents_buff_dict)
    first_market = tuple(db[buff_list[-1]][0:2])
    residents_first_market = tuple(db[residents_buff_list[-1]][0:2])
    return first_market


def task2(db):
    global buff_dict
    global buff_list
    """
    Задача 2
    Args:
        db (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
        помимо database могут быть любые другие аргументы
    Returns:
        list: координаты домов [(x1,y1), (x2,y2) ... (xn,yn)]
    """
    result_lst = [first_market]

    markets_amount = 1
    i = 2
    while markets_amount < 10:
        try:
            x_new = db[buff_list[-i]][0]
            y_new = db[buff_list[-i]][1]
        except:
            return result_lst

        # print(dist_markets)
        flag = True
        for x, y in result_lst:
            dist_markets = distance(x, y, x_new, y_new)
            if dist_markets <= 1:
                flag = False
                break
        if flag:
            markets_amount += 1
            result_lst.append((x_new, y_new))
        i += 1
    return result_lst


def task3(db):
    """
    Задача 3
    Args:
        db (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
        помимо database могут быть любые другие аргументы
    Returns:
        list: координаты домов [(x1,y1), (x2,y2) ... (xn,yn)]
    """
    global residents_buff_dict
    global residents_buff_dict

    result_lst = [residents_first_market]

    markets_amount = 1
    i = 2
    while markets_amount < 15:
        try:
            x_new = db[residents_buff_list[-i]][0]
            y_new = db[residents_buff_list[-i]][1]
        except:
            return result_lst

        # print(dist_markets)
        flag = True
        for x, y in result_lst:
            dist_markets = distance(x, y, x_new, y_new)
            if dist_markets <= 1:
                flag = False
                break
        if flag:
            markets_amount += 1
            result_lst.append((x_new, y_new))
        i += 1
    return result_lst


def plot(database, best_coords):
    # print(best_coords)
    """
    НЕ МЕНЯТЬ КОД!
    Отрисовка точек 2D
    Args:
        database (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
        best_coords (list): для задачи 1 это (x, y), для задачи 2-3 это [(x1,y1), (x2,y2) ... (xn,yn)]
    """
    plt.close()
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.plot([coord[0] for coord in database.values()],
             [coord[1] for coord in database.values()], '.', ms=5, color='k', alpha=0.5)
    if isinstance(best_coords[0], tuple):
        for x, y in best_coords:
            circle = plt.Circle((x, y), 0.5, color='r', fill=False, zorder=2)
            ax.add_patch(circle)
        plt.plot([coord[0] for coord in best_coords],
                 [coord[1] for coord in best_coords], '.', ms=15, color='r')
    elif isinstance(best_coords[0], float):
        x, y = best_coords
        circle = plt.Circle((x, y), 0.5, color='r', fill=False, zorder=2)
        ax.add_patch(circle)
        plt.plot(*best_coords, '.', ms=15, color='r')
    else:
        raise ValueError("Проверь, что подаёшь список кортежей или кортеж из двух координат")
    plt.show()


def homework():
    path = "./buildings"
    database = read_data(path)

    best_task1 = task1(database)
    plot(database, best_task1)

    best_task2 = task2(database)
    plot(database, best_task2)
    #
    best_task3 = task3(database)
    plot(database, best_task3)


if __name__ == '__main__':
    homework()
