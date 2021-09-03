def low_letters_counter(pw):
    counter = 0
    for elem in pw:
        if elem.islower():
            counter += 1
    return counter


def upper_letters_counter(pw):
    counter = 0
    for elem in pw:
        if elem.isupper():
            counter += 1
    return counter


def digits_counter(pw):
    counter = 0
    for elem in pw:
        if elem.isdigit():
            counter += 1
    return counter


def sym_counter(pw):
    counter = 0
    for elem in pw:
        if not elem.isalpha():
            counter += 1
    return counter


def pass_checker(pw):
    if sym_counter(pw) >= 2 and digits_counter(pw) >= 2 and upper_letters_counter(pw) >= 2 and low_letters_counter(
            pw) >= 2 and len(pw) > 8:
        return True
    else:
        return False


print(pass_checker('G1#!nbP0_123'))
print(pass_checker('G#!nbP_1'))
