import xlwt

"""
NOTES:
    =COUNTIF(B73:P73,VALUE(2))
    =COUNTIF(B73:P73,VALUE(3))
    =MIN(Q73:R73)
"""

style0 = xlwt.easyxf(
    "font: name Times New Roman, color-index red, bold on", num_format_str="#,##0.00"
)


def create_workbook(nlist):
    wb = xlwt.Workbook()
    primes_ws = wb.add_sheet("Prime Factorizations")
    twin_primes_ws = wb.add_sheet("Twin Primes")
    twin_primes_ws.write(0, 0, "TP Index", style0)
    twin_primes_ws.write(0, 1, "Twin Prime Pair", style0)
    twin_primes_ws.write(0, 2, "Gap to next twin prime", style0)
    twin_primes_ws.write(0, 3, "Gap since last twin prime", style0)
    twin_primes_ws.write(0, 4, "Primes since last TP", style0)
    twin_primes_ws.write(0, 5, "Multiples of 6 for between number", style0)
    twin_primes_ws.write(0, 6, "Between number", style0)
    twin_primes_ws.write(0, 7, "Factors of between number", style0)

    tp_index = 1
    for num in range(1, len(nlist)):
        primes_ws.write(num, 0, num)
        for index, factor in enumerate(nlist[str(num)]["factors"]):
            primes_ws.write(num, index + 1, factor)
        # write to the twin primes page if we are looking at a twin prime
        if (
            "between_twin_prime" in nlist[str(num)].keys()
            and nlist[str(num)]["between_twin_prime"] is True
        ):
            twin_primes_ws.write(tp_index, 0, tp_index)
            twin_primes_ws.write(tp_index, 1, f"({num - 1}, {num + 1})")
            twin_primes_ws.write(tp_index, 2, nlist[str(num)]["next_tp_gap"])
            twin_primes_ws.write(tp_index, 3, nlist[str(num)]["last_tp_gap"])
            factors = nlist[str(num)]["factors"]

            twos = [i for i in factors if i == 2]
            threes = [i for i in factors if i == 2]

            twin_primes_ws.write(
                tp_index, 4, nlist[str(num - 1)]["primes_since_last_twin_prime"]
            )
            twin_primes_ws.write(tp_index, 5, min(len(twos), len(threes)))
            # twin_primes_ws.write(tp_index, 4, 0)
            twin_primes_ws.write(tp_index, 6, num)
            for index, factor in enumerate(nlist[str(num)]["factors"]):
                twin_primes_ws.write(tp_index, index + 7, factor)
            tp_index += 1

    wb.save("primes-0.1.0.xls")
