import os
import xlwt

"""
NOTES:
    =COUNTIF(B73:P73,VALUE(2))
    =COUNTIF(B73:P73,VALUE(3))
    =MIN(Q73:R73)
"""

headers_style = xlwt.easyxf(
    "font: name Times New Roman, color-index red, bold on", num_format_str="#,##0.00"
)

factor_count_limit = 174


def create_workbook(nlist):
    wb = xlwt.Workbook()
    create_primes_sheet(wb, nlist)
    create_twin_primes_sheet(wb, nlist)
    create_twin_primes_factorizations_sheet(wb, nlist)

    worksheet_version = os.getenv("WORKSHEET_VERSION")
    wb.save(f"primes-{worksheet_version}.xls")


def create_primes_sheet(wb, nlist):
    primes_ws = wb.add_sheet("Prime Factorizations")
    for num in range(1, len(nlist)):
        primes_ws.write(num, 0, num)
        for index, factor in enumerate(nlist[str(num)]["factors"]):
            primes_ws.write(num, index + 1, factor)


def create_twin_primes_sheet(wb, nlist):
    twin_primes_ws = wb.add_sheet("Twin Primes")
    write_twin_primes_headers(twin_primes_ws)
    tp_index = 1
    for num in range(1, len(nlist)):
        # write to the twin primes page if we are looking at a twin prime
        if (
            "between_twin_prime" in nlist[str(num)].keys()
            and nlist[str(num)]["between_twin_prime"] is True
        ):
            write_twin_primes_row(tp_index, num, twin_primes_ws, nlist)
            tp_index += 1


def write_twin_primes_headers(twin_primes_ws):
    twin_primes_ws.write(0, 0, "TP Index", headers_style)
    twin_primes_ws.write(0, 1, "Twin Prime Pair", headers_style)
    twin_primes_ws.write(0, 2, "Gap to next twin prime", headers_style)
    twin_primes_ws.write(0, 3, "Gap since last twin prime", headers_style)
    twin_primes_ws.write(0, 4, "Primes since last TP", headers_style)
    twin_primes_ws.write(0, 5, "Multiples of 6 for between number", headers_style)
    twin_primes_ws.write(0, 6, "Between number", headers_style)
    twin_primes_ws.write(0, 7, "Factors of between number", headers_style)


def write_twin_primes_row(tp_index, num, twin_primes_ws, nlist):
    twin_primes_ws.write(tp_index, 0, tp_index)
    twin_primes_ws.write(tp_index, 1, f"({num - 1}, {num + 1})")
    twin_primes_ws.write(tp_index, 2, nlist[str(num)]["next_tp_gap"])
    twin_primes_ws.write(tp_index, 3, nlist[str(num)]["last_tp_gap"])
    factors = nlist[str(num)]["factors"]

    twos = [i for i in factors if i == 2]
    threes = [i for i in factors if i == 3]

    twin_primes_ws.write(
        tp_index, 4, nlist[str(num - 1)]["primes_since_last_twin_prime"]
    )
    twin_primes_ws.write(tp_index, 5, min(len(twos), len(threes)))
    # twin_primes_ws.write(tp_index, 4, 0)
    twin_primes_ws.write(tp_index, 6, num)
    for index, factor in enumerate(nlist[str(num)]["factors"]):
        twin_primes_ws.write(tp_index, index + 7, factor)


def create_twin_primes_factorizations_sheet(wb, nlist):
    twin_primes_ws = wb.add_sheet("Twin Primes with Factorizations")
    write_twin_primes_factorizations_headers(twin_primes_ws, nlist)
    tp_index = 1
    for num in range(1, len(nlist)):
        # write to the twin primes page if we are looking at a twin prime
        if (
            "between_twin_prime" in nlist[str(num)].keys()
            and nlist[str(num)]["between_twin_prime"] is True
        ):
            write_twin_primes_factorizations_row(tp_index, num, twin_primes_ws, nlist)
            tp_index += 1


def write_twin_primes_factorizations_headers(twin_primes_ws, nlist):
    twin_primes_ws.write(0, 0, "TP Index", headers_style)
    twin_primes_ws.write(0, 1, "Twin Prime Pair", headers_style)
    twin_primes_ws.write(0, 2, "Gap to next twin prime", headers_style)
    twin_primes_ws.write(0, 3, "Gap since last twin prime", headers_style)
    twin_primes_ws.write(0, 4, "Primes since last TP", headers_style)
    index = 1
    for num in range(1, factor_count_limit):
        if nlist[str(num)]["is_prime"] is True:
            twin_primes_ws.write(0, index + 4, f"count of {num} in gap", headers_style)
            index += 1


def write_twin_primes_factorizations_row(tp_index, num, twin_primes_ws, nlist):
    twin_primes_ws.write(tp_index, 0, tp_index)
    twin_primes_ws.write(tp_index, 1, f"({num - 1}, {num + 1})")
    twin_primes_ws.write(tp_index, 2, nlist[str(num)]["next_tp_gap"])
    twin_primes_ws.write(tp_index, 3, nlist[str(num)]["last_tp_gap"])

    twin_primes_ws.write(
        tp_index, 4, nlist[str(num - 1)]["primes_since_last_twin_prime"]
    )
    factor_counts = count_factors_in_gap(num, nlist)
    index = 1
    for i in range(1, factor_count_limit):
        if nlist[str(i)]["is_prime"] is True:
            twin_primes_ws.write(tp_index, index + 4, factor_counts[str(i)])
            index += 1


def count_factors_in_gap(num, nlist):
    factor_counts = {}
    for j in range(1, factor_count_limit):
        if nlist[str(j)]["is_prime"] is True:
            factor_counts[str(j)] = 0

    for j in range(1, factor_count_limit):
        if nlist[str(j)]["is_prime"] is True:
            factor_counts[str(j)] += len(
                [n for n in nlist[str(num)]["factors"] if n == j]
            )

    for i in range(num + 1, len(nlist) - 1):
        for j in range(1, factor_count_limit):
            if nlist[str(j)]["is_prime"] is True:
                factor_counts[str(j)] += len(
                    [n for n in nlist[str(i)]["factors"] if n == j]
                )
        if (
            "between_twin_prime" in nlist[str(i)].keys()
            and nlist[str(i)]["between_twin_prime"] is True
        ):
            break
    return factor_counts
