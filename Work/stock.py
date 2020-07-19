# stock.py
from typedproperty import typedproperty


String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)


class Stock:
    # __slots__ = ['name', 'shares', 'price']
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, cnt):
        assert 0 <= cnt <= self.shares
        self.shares -= cnt

    def __repr__(self):
        return f"Stock({self.name!r}, {self.shares!r}, {self.price!r})"
