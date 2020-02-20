import random
ls = []
for i in range(ord('a'), ord('z') + 1):
    ls.append(chr(i))
for i in range(ord('A'), ord('Z') + 1):
    ls.append(chr(i))
for i in range(ord('1'), ord('9') + 1):
    ls.append(chr(i))

ls_pwd = []
for j in range(61):
    ls2 = ls.copy()
    pwd = ''
    for k in range(8):
        while k == 0:
            random_index = random.randint(0, len(ls2)-1)
            random_value = ls2[random_index]
            pwd += ls2.pop(random_index)
            for m in ls_pwd:
                if m[0] == pwd:
                    ls2.insert(random_index, random_value)
                    pwd = ''
                    break
            else:
                break
        pwd += ls2.pop(random.randint(0, len(ls2)-1))
    ls_pwd.append(pwd)

ls_one = []
for one in ls_pwd:
    ls_one.append(one[0])
print(len(set(ls_one)))


# print(ls_pwd)
