inp = ''''Wazzzzzuuuup bro haw ware youuuozw
Zupppawazup ooo www zuuuppzup wupaz
wupaz zoooo wzauuuuuppp ppppuz waz
zaw upppzwaa uu zwa zwa'''

splitted = inp.split()
print(splitted)
res = []
for i in splitted:
    if len(i) > 5:
        flag = True
        for j in i:
            if j.lower() in ["w", "a", "z", "u", "p"]:
                print(j)
                flag = False
        if flag:
            res.append(i)

print(res)
