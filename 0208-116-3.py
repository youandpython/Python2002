import random


ls = []
for i in range(ord('a'), ord('z') + 1):
    ls.append(chr(i))
for i in range(ord('A'), ord('Z') + 1):
    ls.append(chr(i))
for i in range(ord('1'), ord('9') + 1):
    ls.append(chr(i))

ls_pwd = []
for j in range(30):
    ls2 = ls.copy()
    pwd = ''
    for k in range(8):
        pwd += ls2.pop(random.randint(0, len(ls2)-1))
    ls_pwd.append(pwd)


print(ls_pwd)
