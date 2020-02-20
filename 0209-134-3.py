import random

file = open('number.txt', 'w')
file_2 = open('num.csv', 'w')

for i in range(10):
    ls = []
    for j in range(10):
        ls.append(str(random.randint(0, 99)))

    file.write(' '.join(ls) + '\n')
    file_2.write(','.join(ls) + '\n')
file.close()
file_2.close()
