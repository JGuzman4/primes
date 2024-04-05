# Python program to print prime factors

import math
import xlwt


# A function to print all prime factors of
# a given number n
def primeFactors(n):
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


style0 = xlwt.easyxf(
    "font: name Times New Roman, color-index red, bold on", num_format_str="#,##0.00"
)

wb = xlwt.Workbook()
ws = wb.add_sheet("Prime Factorizations")

for x in range(1, 65536):
    primes = primeFactors(x)
    # print(f"primes for {x}: {primes}")

    ws.write(x, 0, x)
    for index, prime in enumerate(primes):
        ws.write(x, index + 1, prime)

wb.save("primes.xls")
