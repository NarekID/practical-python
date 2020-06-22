# report.py
#
# Exercise 2.4
import sys
import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(f)
        for row in rows:
            d = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(d)
    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


def make_report(portfolio, prices):
    changes = []
    for stock in portfolio:
        changes.append((stock['name'], stock['shares'], round(prices[stock['name']], 2), prices[stock['name']] - stock['price']))
    return changes


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

portfolio_value = 0
current_value = 0

for stock in portfolio:
    portfolio_value += stock['shares'] * stock['price']
    current_value += stock['shares'] * prices[stock['name']]

total_value = current_value - portfolio_value

print(f'Old value: {portfolio_value}')
print(f'Current value: {current_value}')

print(f'Gain: {total_value:0.2f}' if total_value > 0 else f'Loss: {-total_value:0.2f}')

headers = ('Name', 'Shares', 'Price', 'Change')
report = make_report(portfolio, prices)
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * 3 + '-' * 10)
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {"$" + str(price):>10s} {change:>10.2f}')