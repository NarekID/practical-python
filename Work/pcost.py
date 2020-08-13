# pcost.py
#
# Exercise 1.27
import sys
import csv


def portfolio_cost(filename):
    s = 0
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    for row_num, row in enumerate(rows, start=1):
        try:
            s += int(row[1]) * float(row[2])
        except ValueError:
            # print(f"Couldn't calculate line: {row}. Wrong or missing data.")
            print(f"Row {row_num}: Couldn't convert: {row}")
    f.close()
    return s


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
