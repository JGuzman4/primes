# Python program to print prime factors

import json
from scripts.graph.graph import graph_primes
from scripts.xlsheets.xlsheets import create_workbook
from scripts.prime.prime import (
    is_prime,
    get_twin_primes,
    prime_factors,
    get_twin_prime_gaps,
    get_between_twin_primes,
)


def main():
    limit = 10001
    nlist = {}

    plist = sorted([n for n in range(1, 1000) if is_prime(n)])

    tlist = get_twin_primes(plist)

    for i in range(1, limit):
        factors = prime_factors(i)
        if i in plist:
            nlist[str(i)] = {"is_prime": True}
        else:
            nlist[str(i)] = {"is_prime": False}

        if i in tlist:
            nlist[str(i)]["twin_prime"] = True
        else:
            nlist[str(i)]["twin_prime"] = False

        nlist[str(i)]["factors"] = factors

    get_between_twin_primes(nlist)
    get_twin_prime_gaps(nlist)

    with open("data.json", "w") as fp:
        json.dump(nlist, fp, indent=4)

    ## Create excel sheet with prime number data
    # create_workbook(nlist)


main()
