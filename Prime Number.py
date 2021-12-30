def prime(num):

    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
            if count == 2:
                break

    if count == 2:
        print("Prime number.")
    else:
        print("Not Prime number")



prime(3)
prime(10)
prime(2)
