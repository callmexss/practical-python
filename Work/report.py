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


if __name__ == "__main__":
    li = read_portfolio("Data/portfolio.csv")
    prices = read_prices("Data/prices.csv")
    total = 0
    print(li)
    for each in li:
        print(each, prices[each['name']])
        total += each['shares'] * (prices[each['name']] - each['price'])
    print(total)
