while True:
    word = input()
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            print('ok')
        else:
            print('not')