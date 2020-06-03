# pcost.py
#
# Exercise 1.27
import sys
import csv


def portfolio_cost(filename):
    s = 0
    f = open(filename)
    rows = csv.reader(f)
    for row in rows:
        try:
            s += int(row[1]) * float(row[2])
        except ValueError:
            print(f"Couldn't calculate line: {row}. Wrong or missing data.")
    f.close()
    return s


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')
