def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True


def nth_prime(x):
    num = 3
    prime = 2

    if x == 1:
        return 2

    while prime < x:
        num += 2
        if is_prime(num):
            prime += 1
    return num

print(nth_prime(3))
print(nth_prime(5))

