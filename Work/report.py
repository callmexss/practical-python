# report.py
#
# Exercise 2.4
import csv
from pprint import pprint


def read_portfolio(filename):
    portfolio_list = []
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            item = dict(zip(header, (row[0], int(row[1]), float(row[2]))))
            portfolio_list.append(item)
    return portfolio_list


def read_prices(filename):
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])
        return prices


def make_report(portfolio, prices):
    result_list = []
    for each in portfolio:
        name = each['name']
        shares = each['shares']
        price = prices[name]
        change = price - each['price']
        result_list.append((name, shares, price, change))
    return result_list


if __name__ == "__main__":
    li = read_portfolio("Data/portfolio.csv")
    prices = read_prices("Data/prices.csv")
    total = 0
    for each in li:
        print(each, prices[each['name']])
        total += each['shares'] * (prices[each['name']] - each['price'])
    print(total)
    header = ('Name', 'Shares', 'Price', 'Change')
    sep = ''
    print('%10s %10s %10s %10s' % header)
    print(f'{sep:->10s} {sep:->10s} {sep:->10s} {sep:->10s}')
    for r in make_report(li, prices):
        # print("%10s %10d %10.2f %10.2f" % r)
        price = '$' + f'{r[2]:.2f}'
        print(f'{r[0]:>10s} {r[1]:>10d} {price:>10s} {r[3]:>10.2f}')
