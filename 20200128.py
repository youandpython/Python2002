# # # # # # # # # n = eval(input('please input a number:'))
# # # # # # # # # print(int(n / 100))
# # # # # # # #
# # # # # # # # n = input('please input a number:')
# # # # # # # # print(n[:-2])
# # # # # # # s = 'abcdefg'
# # # # # # # print(s[:])
# # # # # # # print(s[:-2])
# # # # # # # print(s[0:-1])
# # # # # # # print(s[2:4])
# # # # # #
# # # # # # s = input('please input a string:')
# # # # # # li = s.split()
# # # # # #
# # # # # # for i in li:
# # # # # #     print(i)
# # # # #
# # # # # week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
# # # # # num = input('please input a number for 1~7:')
# # # # # num = eval(num)
# # # # # if 1 <= num <= 7:
# # # # #     print(week[num - 1])
# # # # #
# # # # num = input('please input a 5 bit number:')
# # # # num2 = num[::-1]
# # # # if num == num2:
# # # #     print('This is a good number.')
# # # # else:
# # # #     print('Nothing.')
# # # # s = '123132131'
# # # # # # # print(len(s))
# # # num = eval(input('please input a number:'))
# # # pri
#
# print(pow(-1, 0.5))
while True:
    num = input('请输入一个年份：')
    try:
        num = int(num)
    except:
        print('输入内容必须为整数！')
        continue
    if num % 400 == 0 or (num % 4 == 0 and num % 100 != 0):
        print('{}是闰年'.format(num))
    else:
        print('{}不是闰年'.format(num))
# while True:
#     num_a = eval(input('please the first number:'))
#     num_b = eval(input('please the second number:'))
#     num_m = 1
#     for i in range(1, (min(num_a, num_b) + 1)):
#         if num_a % i == 0 and num_b % i == 0:
#             num_m = i
#     print('{}是最大公约数。'.format(num_m))
#     print('{}是最小公倍数。'.format(int(num_a * num_b / num_m)))
# while True:
#     s = input('please input a lot of word:')
#     space = 0
#     num = 0
#     letter = 0
#     other = 0
#     for i in s:
#         if i == ' ':
#             space += 1
#         elif 0x0030 <= ord(i) <= 0x0039:
#             num += 1
#         elif 'a' <= i <= 'z' or 'A' <= i <= 'Z':
#             letter += 1
#         else:
#             other += 1
#     print('空格有{}个，数字有{}个，字母有{}个，其它有{}个'.format(space, num, letter, other))
