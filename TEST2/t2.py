inp = ''''Wazzzzzuuuup bro haw ware youuuozw
Zupppawazup ooo www zuuuppzup wupaz
wupaz zoooo wzauuuuuppp ppppuz waz
zaw upppzwaa uu zwa zwa'''

splitted = inp.split()
alph = ["w", "a", "z", "u", "p"]
res = []
for word in splitted:
    if len(word) > 5:
        flag = True
        for letter in alph:
            if not(letter in word.lower()):
                flag = False
        if flag:
            res.append(word)

print(res)
