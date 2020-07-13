# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    portfolio_list = []
    with open(filename) as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            portfolio_list.append((row[0], int(row[1]), float(row[2])))
    return portfolio_list


li = read_portfolio("Data/portfolio.csv")
print(li)



