# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):
    cost = 0
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)  # get csv header
        for i, row in enumerate(rows, 0):
            record = dict(zip(header, row))
            try:
                share = record['shares']
                price = record['price']
                cost += int(share) * float(price)
            except ValueError:
                field1 = "share" if not share else ''
                field2 = "price" if not price else ''
                print(f"Row {i}: Bad row: {row}")
    return cost


cost = portfolio_cost("Data/portfolio.csv")
# print(f"Total cost {cost}")

cost = portfolio_cost("Data/missing.csv")

if __name__ == "__main__":
    sys.argv.append("Data/portfoliodate.csv")
    filename = sys.argv[1]
    cost = portfolio_cost(filename)
    print(f"Total cost {cost}")

