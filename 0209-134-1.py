
file = open('word.txt', 'r')
s = file.read()
ch = input('please input a character:')
counter = 0
for i in s:
    if ch == i:
        counter += 1
print('counter is {}.'.format(counter))

