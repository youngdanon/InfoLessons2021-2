n = input()


def sum_of_num(n):
    summ = 0
    for i in range(len(n)):
        summ += int(n[i])
    # print(summ)
    return str(summ)


def summarize(n):
    if len(n) > 1:
        return summarize(sum_of_num(n))
    else:
        return n


print(summarize(n))
