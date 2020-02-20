s = input('please input a string:')
s = s.lower()
for ch in '!,. ':
    s = s.replace(ch, '')
print(s)
letters = {}
for letter in s:
    letters[letter] = letters.get(letter, 0) + 1
items = list(letters.items())
items.sort(key=lambda x: x[1], reverse=True)
for val in items:
    # print(val[0], val[1])
    print('{}:{}'.format(val[0], val[1]))
