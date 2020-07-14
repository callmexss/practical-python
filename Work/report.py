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
            stock = {
                    'name': record['name'],
                    'shares': int(record['shares']),
                    'price': float(record['price']),
                    }
            portfolio_list.append(stock)
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


def print_report(report):
    header = ('Name', 'Shares', 'Price', 'Change')
    sep = ''
    print('%10s %10s %10s %10s' % header)
    print(f'{sep:->10s} {sep:->10s} {sep:->10s} {sep:->10s}')
    for r in report:
        # print("%10s %10d %10.2f %10.2f" % r)
        price = '$' + f'{r[2]:.2f}'
        print(f'{r[0]:>10s} {r[1]:>10d} {price:>10s} {r[3]:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


if __name__ == "__main__":
    # portfolio = read_portfolio("Data/portfoliodate.csv")
    # prices = read_prices("Data/prices.csv")

    # total = 0
    # for each in portfolio:
    #     print(each, prices[each['name']])
    #     total += int(each['shares']) * (prices[each['name']] - float(each['price']))
    # print(total)

    # report = make_report(portfolio, prices)
    # print_report(report)
    files = ['Data/portfolio.csv', 'Data/portfolio2.csv']
    for name in files:
        print(f'{name:-^43s}')
        portfolio_report(name, 'Data/prices.csv')
        print()

