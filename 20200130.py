# # try:
# #     n = eval(input('please input a number:'))
# #     print('输入数字的3次方值为：', n**3)
# # except:
# #     print('输入错误，请输入一个数字！')
#
# try:
#     for i in range(5):
#         print(10 / i, end=' ')
# except:
#     print('某种原因，出错了！')
#
import random
target = random.randint(1, 1000)
count = 0
while True:
    guess = eval(input('请输入你猜测的一个整数(1至1000）：'))
    count += 1
    if guess > target:
        print('猜大了')
    elif guess < target:
        print('猜小了')
    else:
        print('猜对了')
        break
print('此轮的猜测次数是：', count)
