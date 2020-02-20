

def prime(number):
    if number == 2:
        return True
    for i in range(2, number//2+1):
        if number % i == 0:
            return True
    else:
        return False


while True:
    try:
        num = eval(input('\nplease input a int number:'))
        for i in range(1, num+1):
            if not prime(i):
                print(i, end=' ')
    except:
        print('you should input a int number!')
