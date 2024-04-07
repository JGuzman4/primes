import xlwt
from ..prime.prime import prime_factors

"""
NOTES:
    =COUNTIF(B73:P73,VALUE(2))
    =COUNTIF(B73:P73,VALUE(3))
    =MIN(Q73:R73)
"""


def create_workbook(nlist):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Prime Factorizations")
    for x in range(1, len(nlist)):
        primes = prime_factors(x)
        ws.write(x, 0, x)
        for index, prime in enumerate(primes):
            ws.write(x, index + 1, prime)

    wb.save("primes-0.1.0.xls")
