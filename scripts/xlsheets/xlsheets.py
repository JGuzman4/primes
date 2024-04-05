import xlwt
from ..prime.prime import prime_factors


def create_workbook():
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Prime Factorizations")
    for x in range(1, 65536):
        primes = prime_factors(x)
        ws.write(x, 0, x)
        for index, prime in enumerate(primes):
            ws.write(x, index + 1, prime)

    wb.save("primes.xls")
