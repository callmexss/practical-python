# report.py
#
# Exercise 2.4
import sys
import csv
from pprint import pprint

from fileparse import parse_csv


def read_portfolio(filename):
    with open(filename) as f:
        return parse_csv(f, select=['name', 'shares', 'price'],
                         types=[str, int, float])


def read_prices(filename):
    with open(filename) as f:
        return dict(parse_csv(f, types=[str, float], has_header=False))
    

def make_report(portfolio, prices):
    result_list = []
    prices = dict(prices)
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


def main(args_li):
    portfolio_report(args_li[1], args_li[2])


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

