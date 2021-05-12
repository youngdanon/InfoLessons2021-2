import random
from threading import Thread

result_max_tuple = []


def max_triple(mas, ranges):
    global result_max_tuple
    max_tuple = ()
    max_sum = 0
    for i in range(ranges[0], ranges[1]):
        current = mas[i:i + 3]
        summ = sum(current)
        if max_sum < summ:
            max_sum = summ
            max_tuple = tuple(j for j in current)
    result_max_tuple.append(max_tuple)


if __name__ == "__main__":
    # inp = [2, 4, 6, 1, -3, 9, -4, 3, 9, 4, 0, 1
    inp = list(random.randint(0, 100) for i in range(1000000))

    proc1 = Thread(target=max_triple, args=(inp, (0, int(len(inp) / 3))))
    proc2 = Thread(target=max_triple, args=(inp, (int(len(inp) / 3), int(len(inp) / 3 * 2))))
    proc3 = Thread(target=max_triple, args=(inp, (int(len(inp) / 3 * 2), len(inp))))

    procs = [proc1, proc2, proc3]

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()

    max_sum = 0
    max_tup = 0
    for tup in result_max_tuple:
        summ = sum(tup)
        if max_sum < summ:
            max_sum = summ
            max_tup = tup
    print(max_tup)


