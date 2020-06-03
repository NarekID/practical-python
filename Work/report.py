# report.py
#
# Exercise 2.4
import sys
import csv


def read_portfolio(filename):
    portfolio = []
    f = open(filename)
    headers = next(f)
    rows = csv.reader(f)
    for row in rows:
        d = {
            'name': row[0],
            'shares': int(row[1]),
            'price': float(row[2])
        }
        portfolio.append(d)
    f.close()
    return portfolio


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

portfolio = read_portfolio(filename)
print(portfolio)

