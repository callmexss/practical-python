# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    cost = 0
    with open(filename) as f:
        start = True
        for line in f:
            if start:
                start = False
                continue
            _, share, price = line.split(",")
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
