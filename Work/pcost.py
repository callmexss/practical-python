# pcost.py
#
# Exercise 1.27

import sys
import csv

import report
from fileparse import parse_csv


def portfolio_cost(filename):
    cost = 0
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
    for record in records:
        try:
            cost += record.cost
        except ValueError:
            print(f"Row {i}: Bad row: {row}")
    return cost


def main(args_li):
    print(f"Total cost {portfolio_cost(args_li[1])}")



# cost = portfolio_cost("Data/portfolio.csv")
# print(f"Total cost {cost}")

# cost = portfolio_cost("Data/missing.csv")

if __name__ == "__main__":
    main(sys.argv)

