# pcost.py
#
# Exercise 1.27
f = open('Data/portfolio.csv', 'r')
next(f)
s = 0
for line in f:
    row = line.strip().split(',')
    s += int(row[1]) * float(row[2])
print(f'Total cost: {s}')
