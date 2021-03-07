from matplotlib import pyplot as plt
from math import hypot
import time

first_market = ()
residents_first_market = ()
buildings_amount_dict = {}
residents_amount_dict = {}
buildings_amount_list = []
residents_amount_list = []


def dict_sorting_by_values(dict):
    return {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}


def check_r_b_amount(db: dict, rad):
    global buildings_amount_dict
    global residents_amount_dict
    global residents_amount_list
    global buildings_amount_list
    for key, value in db.items():
        buildings_amount = 0
        residents_amount = 0
        for elem2 in db.values():
            if value != elem2:
                if hypot(value[0] - elem2[0], value[1] - elem2[1]) <= rad:
                    buildings_amount += 1
                    residents_amount += elem2[2] * 0.7 / 18
                    residents_amount_dict.update({key: residents_amount})
                    buildings_amount_dict.update({key: buildings_amount})
    residents_amount_dict = dict_sorting_by_values(residents_amount_dict)
    buildings_amount_dict = dict_sorting_by_values(buildings_amount_dict)
    residents_amount_list = list(residents_amount_dict)
    buildings_amount_list = list(buildings_amount_dict)


def read_data(path):
    database = {}
    with open("./buildings", encoding="utf-8") as file:
        for line in file:
            raw_row = line.split("\t")
            database.update({raw_row[0]: tuple(map(float, raw_row[1:4]))})
    return database


def task1(db):
    global first_market
    global residents_first_market
    check_r_b_amount(db, 0.5)
    first_market = tuple(db[buildings_amount_list[-1]][0:2])
    residents_first_market = tuple(db[residents_amount_list[-1]][0:2])
    return first_market


def task2(db):
    result_lst = [first_market]
    markets_amount = 1
    i = 2
    while markets_amount < 10:
        x_new = db[buildings_amount_list[-i]][0]
        y_new = db[buildings_amount_list[-i]][1]
        flag = True
        for x, y in result_lst:
            if hypot(x - x_new, y - y_new) <= 1:
                flag = False
                break
        if flag:
            markets_amount += 1
            result_lst.append((x_new, y_new))
        i += 1
    return result_lst


def task3(db):
    result_lst = [residents_first_market]
    markets_amount = 1
    i = 2
    while markets_amount < 15:
        x_new = db[residents_amount_list[-i]][0]
        y_new = db[residents_amount_list[-i]][1]
        flag = True
        for x, y in result_lst:
            if hypot(x - x_new, y - y_new) <= 1:
                flag = False
                break
        if flag:
            markets_amount += 1
            result_lst.append((x_new, y_new))
        i += 1
    return result_lst


def plot(database, best_coords):
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
    best_task3 = task3(database)
    plot(database, best_task3)


if __name__ == '__main__':
    timer = time.time()
    homework()
    stop_timer = time.time()
    timing = stop_timer - timer
    print(timing)
