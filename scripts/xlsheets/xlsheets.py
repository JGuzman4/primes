import xlwt

"""
NOTES:
    =COUNTIF(B73:P73,VALUE(2))
    =COUNTIF(B73:P73,VALUE(3))
    =MIN(Q73:R73)
"""


def create_workbook(nlist):
    wb = xlwt.Workbook()
    primes_ws = wb.add_sheet("Prime Factorizations")
    twin_primes_ws = wb.add_sheet("Twin Primes")
    tp_index = 1
    for num in range(1, len(nlist)):
        primes_ws.write(num, 0, num)
        for index, factor in enumerate(nlist[str(num)]["factors"]):
            primes_ws.write(num, index + 1, factor)
        if (
            "between_twin_prime" in nlist[str(num)].keys()
            and nlist[str(num)]["between_twin_prime"] is True
        ):
            twin_primes_ws.write(tp_index, 0, f"({num - 1}, {num + 1})")
            twin_primes_ws.write(tp_index, 1, num)
            for index, factor in enumerate(nlist[str(num)]["factors"]):
                twin_primes_ws.write(tp_index, index + 2, factor)
            tp_index += 1
    # for x in range(1, len(nlist)):
    #    factors = prime_factors(x)
    #    primes_ws.write(x, 0, x)
    #    for index, prime in enumerate(factors):
    #        primes_ws.write(x, index + 1, prime)

    wb.save("primes-0.1.0.xls")
