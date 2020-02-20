# a = 1
# b = 2
# i = 2
# m = eval(input('please input the serial number:'))
#
# while True:
#     a, b = b, a+b
#     i += 1
#     if i == m:
#         print(i, b)
#         break


def num(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return num(n-1) + num(n-2)


print(num(8))

