# ticker.py


import csv

import report
from tableformat import create_formatter, print_table
from follow import follow


def parse_stock_data(lines):
    rows = csv.reader(lines)
    return rows


def select_columns(rows, indices):
    for row in rows:
        yield [row[i] for i in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def filter_symbols(rows, names):
    return (row for row in rows if row['name'] in names)


def ticker(portfile, logfile, fmt):
    names = ['name', 'price', 'change']
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = select_columns(rows, [0, 1, 4])
    rows = make_dicts(rows, names)
    rows = filter_symbols(rows, portfolio)
    formatter = create_formatter(fmt)
    formatter.headings([name.title() for name in names])
    for row in rows:
        formatter.row([row['name'], row['price'], row['change']])


if __name__ == "__main__":
    # lines = follow("Data/stocklog.csv")
    # rows = parse_stock_data(lines)
    # rows = select_columns(rows, [0, 1, 4])
    # rows = convert_types(rows, [str, float, float])
    # rows = make_dicts(rows, ['name', 'price', 'change'])
    # for row in rows:
    #     print(row)

    # import report
    # portfolio = report.read_portfolio('Data/portfolio.csv')
    # rows = parse_stock_data(follow('Data/stocklog.csv'))
    # rows = make_dicts(rows, ['name', 'price', 'change'])
    # rows = filter_symbols(rows, portfolio) 
    # for row in rows:
    #     print(row)

    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'csv')
