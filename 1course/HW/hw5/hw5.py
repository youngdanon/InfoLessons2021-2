def dict_sorting_by_values(d):
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}


with open("./war_n_peace.txt", encoding="utf-8") as file:
    line_counter = 0
    word_counter = 0
    res_lst = []
    words_dict = {}
    letters_dict = {}
    for line in file:
        if "Princesse, ma parole" in line:
            print(f'Princesse, ma parole found in {line_counter}')

        line = line.replace("Анна Павловна", "Anna Pavlovna")

        res_lst += line.split()
        line_counter += 1
print(f'4) {len(res_lst)}')

res_lst = list(map(str.lower, res_lst))
# print(res_lst)
check_rus_let = lambda a: True if ord("я") >= ord(a) >= ord("а") else False

res_lst = list(filter(lambda a: a, map(lambda a: "".join(filter(check_rus_let, a)), res_lst)))

# res_lst = list(map())
# print(res_lst)
letters_quantity = sum(map(len, res_lst))
average_len = letters_quantity / len(res_lst)
print(f'7) {average_len}')
print(f'8) {letters_quantity}')

for word in res_lst:
    if word in words_dict:
        words_dict.update({word: words_dict[word] + 1})
    else:
        words_dict.update({word: 1})

    for letter in word:
        if letter in letters_dict:
            letters_dict.update({letter: letters_dict[letter] + 1})
        else:
            letters_dict.update({letter: 1})

words_top = [(k, v,) for k, v in dict_sorting_by_values(words_dict).items()]
letters_top = [(k, v,) for k, v in dict_sorting_by_values(letters_dict).items()]
print(f'10) {words_top[-1:-11:-1]}')
print(f'11) {letters_top[-1:-11:-1]}' )

# print(words_top)
# print(res_lst)
