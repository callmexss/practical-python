# report.py
#
# Exercise 2.4
import sys
import csv
from pprint import pprint

import tableformat
from fileparse import parse_csv
from stock import Stock


def read_portfolio(filename):
    with open(filename) as f:
        records = parse_csv(f, select=['name', 'shares', 'price'],
                         types=[str, int, float])
        return [Stock(r['name'], r['shares'], r['price']) for r in records]


def read_prices(filename):
    with open(filename) as f:
        return dict(parse_csv(f, types=[str, float], has_header=False))
    

def make_report(portfolio, prices):
    result_list = []
    prices = dict(prices)
    for each in portfolio:
        name = each.name
        shares = each.shares
        price = prices[name]
        change = price - each.price
        result_list.append((name, shares, price, change))
    return result_list


def print_report(reportdata, formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    # sep = ''
    # print('%10s %10s %10s %10s' % header)
    # print(f'{sep:->10s} {sep:->10s} {sep:->10s} {sep:->10s}')
    for name, shares, price, change in reportdata:
        # print("%10s %10d %10.2f %10.2f" % r)
        price = '$' + f'{price:.2f}'
        rowdata = [name, str(shares), price, f'{change:.2f}']
        formatter.row(rowdata)
        # print(f'{r[0]:>10s} {r[1]:>10d} {price:>10s} {r[3]:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    """Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args_li):
    if len(args_li) == 3:
        portfolio_report(args_li[1], args_li[2])
    elif len(args_li) == 4:
        portfolio_report(args_li[1], args_li[2], args_li[3])
    else:
        print("Invalid arguments")


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
    args_li = sys.argv
    main(args_li)

