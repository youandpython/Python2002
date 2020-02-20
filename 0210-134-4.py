# coding=utf-8
def search_keyword_index(s):
    key_word = ['and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
                'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'None',
                'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'True', 'try', 'with', 'while', 'yield']
    index_list = []
    for word in key_word:
        index_beg = 0
        while word in s[index_beg:]:
            word_begin_index = s.index(word, index_beg, len(s))
            index_list += [i for i in range(word_begin_index, word_begin_index+len(word))]
            index_beg = word_begin_index + len(word)
    index_list.sort()
    return index_list


file_read = open('pdf.py', 'r')
s_read = file_read.read()
file_read.close()

file_write = open('pdf_write.py', 'w')
s_write = ''
for index in range(len(s_read)):  # 两种方法和下面的一样
    if ('a' <= s_read[index] <= 'z') and (index not in search_keyword_index(s_read)):
        s_write += s_read[index].upper()
    else:
        s_write += s_read[index]

# 两种方法和上面的一样
# for index in range(len(s_read)):
#     if ('a' <= s_read[index] <= 'z') and (index not in search_keyword_index(s_read)):
#         s_read = s_read[:index] + s_read[index].upper() + s_read[(index + 1):]

print(s_write)
file_write.write(s_write)
file_write.close()

