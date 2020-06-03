# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    s = 0
    with open(filename, 'r') as f:
        for line in f:
            row = line.split(',')
            try:
                s += int(row[1]) * float(row[2])
            except ValueError:
                print(f"Couldn't calculate line: {line}")
    return s

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost: {cost}')
