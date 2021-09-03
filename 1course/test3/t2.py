def max_triple(mas):
    max_tuple = ()
    max_sum = 0
    for i in range(0, len(mas) - 3):
        current = mas[i:i + 3]
        summ = sum(current)
        if max_sum < summ:
            max_sum = summ
            max_tuple = tuple(j for j in current)
    return max_tuple


print(max_triple([2, 4, 6, 1, -3, 9, -4, 3, 9, 4, 0, 1]))
