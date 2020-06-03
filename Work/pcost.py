# pcost.py
#
# Exercise 1.27
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

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost: {cost}')
