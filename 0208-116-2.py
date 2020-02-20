s = input('please input a string:')
for ch in '!,. ，。':
    s = s.replace(ch, '')
letters = {}
for letter in s:
    letters[letter] = letters.get(letter, 0) + 1
items = list(letters.items())
items.sort(key=lambda x: x[1], reverse=True)
for val in items:
    print('{}:{}'.format(val[0], val[1]))
