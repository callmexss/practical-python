# stock.py

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, cnt):
        assert 0 <= cnt <= self.shares
        self.shares -= cnt

    def __repr__(self):
        return f"Stock({self.name!r}, {self.shares!r}, {self.price!r})"
