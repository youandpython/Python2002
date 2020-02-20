ls = [6, 'True', '北京', '上海', '天津', 66, '重庆', 1, True, 0.8, 0.5, '3+5j', 13+8j, 'abc', 'False', '我们的祖国，是花园']
ls2 = []
for i in ls:
    if str(i) != i:
        ls2.append(str(i))
        continue
    ls2.append(i)
f = open('city.csv', 'w')
f.write(','.join(ls2)+'\n')
f.close()
f = open('city.csv', 'r')
ls = f.read().strip('\n').split(',')
f.close()

ls3 = []
for i in ls:
    try:
        if eval(i) == complex(i) or eval(i) == float(i):
            ls3.append(eval(i))
    except:
            ls3.append(i)

print(ls3)
