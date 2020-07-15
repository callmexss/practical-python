# pcost.py
#
# Exercise 1.27

import sys
import csv


from fileparse import parse_csv

def portfolio_cost(filename):
    cost = 0
    records = parse_csv(filename, select=['shares', 'price'], types=[int, float])
    for record in records:
        try:
            share = record['shares']
            price = record['price']
            print(share, price)
            cost += share * price
        except ValueError:
            print(f"Row {i}: Bad row: {row}")
        except TypeError:
            print(record)
    return cost


cost = portfolio_cost("Data/portfolio.csv")
# print(f"Total cost {cost}")

cost = portfolio_cost("Data/missing.csv")

if __name__ == "__main__":
    sys.argv.append("Data/portfoliodate.csv")
    filename = sys.argv[1]
    cost = portfolio_cost(filename)
    print(f"Total cost {cost}")

