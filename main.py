## Python program to print prime factors

import json
import sympy
from scripts.graph.graph import create_plot
from scripts.xlsheets.xlsheets import create_workbook
from scripts.prime.prime import (
    get_twin_primes,
    prime_factors,
    get_twin_prime_gaps,
    get_between_twin_primes,
)


def main():
    limit = 40001
    nlist = {}

    plist = list(sympy.primerange(0, limit))

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

    # nums = range(limit)
    # create_plot(nums, figsize=10, s=0.4)
    ## Create excel sheet with prime number data
    create_workbook(nlist)


main()
