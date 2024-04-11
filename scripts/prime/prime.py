import math

import sympy


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


def is_prime(n):
    if n > 1:
        # Iterate from 2 to n // 2
        for i in range(2, (n // 2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False


def get_prime_info(limit):
    nlist = {}
    plist = list(sympy.primerange(0, limit))
    tlist = get_twin_primes(plist)
    for i in range(1, limit):
        if i in plist:
            nlist[str(i)] = {"is_prime": True}
        else:
            nlist[str(i)] = {"is_prime": False}

        if i in tlist:
            nlist[str(i)]["twin_prime"] = True
        else:
            nlist[str(i)]["twin_prime"] = False

        nlist[str(i)]["factors"] = prime_factors(i)
    return nlist


def get_twin_primes(plist):
    tlist = []
    for i, p in enumerate(plist):
        if i < len(plist) - 1 and plist[i + 1] - p == 2:
            tlist.append(p)
            tlist.append(plist[i + 1])
    return tlist


def get_between_twin_primes(nlist):
    # loop up to 10000
    nlist[str(1)]["between_twin_prime"] = False
    for i in range(2, len(nlist) - 1):
        if (
            nlist[str(i - 1)]["twin_prime"] is True
            and nlist[str(i + 1)]["twin_prime"] is True
        ):
            nlist[str(i)]["between_twin_prime"] = True
        else:
            nlist[str(i)]["between_twin_prime"] = False


def get_twin_prime_gaps(nlist):
    # statically set this value for 3, since we know this case to always be 0
    nlist[str(3)]["primes_since_last_twin_prime"] = 0
    for i in range(2, len(nlist) - 1):
        if nlist[str(i)]["between_twin_prime"] is True:
            get_next_gap_info(nlist, i)
            get_last_gap_info(nlist, i)


def get_next_gap_info(nlist, i):
    prime_count = 0
    for j in range(i + 2, len(nlist) - 1):
        if nlist[str(j)]["between_twin_prime"] is True:
            nlist[str(j - 1)]["primes_since_last_twin_prime"] = (
                0 if prime_count == 0 else prime_count - 1
            )
            nlist[str(i)]["next_tp_gap"] = j - i
            return
        if nlist[str(j)]["is_prime"] is True:
            prime_count += 1
    nlist[str(i)]["next_tp_gap"] = -1


def get_last_gap_info(nlist, i):
    prime_count = 0
    for j in range(i - 2, 1, -1):
        if nlist[str(j)]["between_twin_prime"] is True:
            nlist[str(j + 1)]["primes_til_next_twin_prime"] = (
                0 if prime_count == 0 else prime_count - 1
            )
            nlist[str(i)]["last_tp_gap"] = i - j
            return
        if nlist[str(j)]["is_prime"] is True:
            prime_count += 1
    nlist[str(i)]["last_tp_gap"] = -1


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
