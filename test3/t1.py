def split_pairs(row):
    result = []
    if len(row) % 2 != 0:
        row += "_"
    for i in range(1, len(row), 2):
        result.append(row[i - 1:i + 1])

    return result


print(split_pairs('abc'))
