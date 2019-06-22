for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("%d is FizzBazz" % num)
    if num % 3 == 0:
        print("%d is Fiz" % num)
    elif num % 5 == 0:
        print("%d is Bazz" % num)


