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
        for i, row in enumerate(rows):
            record = dict(zip(header, row))
            portfolio_list.append(record)
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
        try:
            name = each['name']
            shares = int(each['shares'])
            price = float(prices[name])
            change = price - float(each['price'])
            result_list.append((name, shares, price, change))
        except ValueError:
            print(f"Row {i}: Bad row: {row}")
    return result_list


if __name__ == "__main__":
    li = read_portfolio("Data/portfoliodate.csv")
    prices = read_prices("Data/prices.csv")
    total = 0
    for each in li:
        print(each, prices[each['name']])
        total += int(each['shares']) * (prices[each['name']] - float(each['price']))
    print(total)
    header = ('Name', 'Shares', 'Price', 'Change')
    sep = ''
    print('%10s %10s %10s %10s' % header)
    print(f'{sep:->10s} {sep:->10s} {sep:->10s} {sep:->10s}')
    for r in make_report(li, prices):
        # print("%10s %10d %10.2f %10.2f" % r)
        price = '$' + f'{r[2]:.2f}'
        print(f'{r[0]:>10s} {r[1]:>10d} {price:>10s} {r[3]:>10.2f}')
