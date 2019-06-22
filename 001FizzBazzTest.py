for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("%d is FizzBazz" % number)
    if number % 3 == 0:
        print("%d is Fiz" % number)
    elif number % 5 == 0:
        print("%d is Bazz" % number)


