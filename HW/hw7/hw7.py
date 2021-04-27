def final_gen(path):
    data = (line for line in open(path))
    summ = sum((int(line.split(';')[-2]) for line in data if line[:-1].split(';')[-1] == 'a'))
    data = (line for line in open(path))
    weight_raised = summ / (30e6 - 10e6) * 1000
    for line in data:
        split_line = line[:-1].split(';')
        if split_line[-1] == 'a' and int(split_line[-2]) < weight_raised:
            result = (split_line[0], split_line[2], split_line[-2])
            yield result


if __name__ == '__main__':
    print(*list(final_gen('dataset')), sep="\n")
