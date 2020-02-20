

def is_prime():

    try:
        n = eval(input('please a int number:'))
        if n == int(n):
            if n == 2:
                return True
            for i in range(2, n // 2 + 1):
                if n % i == 0:
                    return True

            else:
                return False
    except:
        print('You should input a int number!')


while True:
    print(is_prime())
