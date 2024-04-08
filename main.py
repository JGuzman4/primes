## Python program to print prime factors

import json
from scripts.graph.graph import create_plot
from scripts.xlsheets.xlsheets import create_workbook
from scripts.prime.prime import (
    get_prime_info,
    get_twin_prime_gaps,
    get_between_twin_primes,
)


def main():
    limit = 40001
    nlist = get_prime_info(limit)

    get_between_twin_primes(nlist)
    get_twin_prime_gaps(nlist)
    create_plot(range(limit), figsize=10, s=0.4)
    create_workbook(nlist)

    with open("data.json", "w") as fp:
        json.dump(nlist, fp, indent=4)


main()
