# pcost.py
#
# Exercise 1.27

import sys
import csv

def portfolio_cost(filename):
    cost = 0
    with open(filename) as f:
        rows = csv.reader(f)
        start = True
        for row in rows:
            if start:
                start = False
                continue
            _, share, price = row
            try:
                cost += int(share) * float(price)
            except ValueError:
                field1 = "share" if not share else ''
                field2 = "price" if not price else ''
                print(f"Missing field {field1} {field2}.")
    return cost


cost = portfolio_cost("Data/portfolio.csv")
print(f"Total cost {cost}")

cost = portfolio_cost("Data/missing.csv")

if __name__ == "__main__":
    filename = sys.argv[1]
    cost = portfolio_cost(filename)
    print(f"Total cost {cost}")

