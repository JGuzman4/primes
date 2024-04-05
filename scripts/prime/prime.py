import math


def nth_prime(n):
    """
    a function to get the nth prime number
    """
    start = 2
    count = 0
    while True:
        if all([start % i for i in range(2, int(math.sqrt(start)) + 1)]) != 0:
            count += 1
            if count == n:
                return start
        start += 1


def prime_factors(n):
    """
    a function to print all prime factors of
    """
    primes = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        primes.append(2)
        n = n // 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # while i divides n , print i ad divide n
        while n % i == 0:
            primes.append(i)
            n = n // i

    if n > 2:
        primes.append(n)
    return primes
