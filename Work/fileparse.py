# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(f,
              select=[],
              types=[],
              has_header=True,
              delimiter=',',
              silence_errors=False):
    """Parse a CSV file into a list of records.
    """
    if select and not has_header:
        raise RuntimeError("select argument requires column headers")

    records = []
    rows = csv.reader(f, delimiter=delimiter)

    header = next(rows) if has_header else ''

    if select:
        indices = [header.index(each) for each in select]
        header = select

    for i, row in enumerate(rows, start=1):
        if not row:
            continue

        if select:
            row = [row[i] for i in indices]

        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as err:
                if not silence_errors:
                    print(f"Row {i}: Couldn't convert {row}")
                    print(f"Row {i}: Reason {err}")
                continue

        if has_header:
            record = dict(zip(header, row))
        else:
            record = tuple(row)
        records.append(record)
    return records


if __name__ == "__main__":
    with open("Data/portfolio.csv") as f:
        records = parse_csv(f)

    with open("Data/portfolio.csv") as f:
        records = parse_csv(f, select=['name', 'shares'])

    with open("Data/portfolio.csv") as f:
        records = parse_csv(f, types=[str, int, float])

    with open("Data/portfolio.csv") as f:
        records = parse_csv(f,
                            select=['name', 'price'],
                            types=[str, float])

    with open("Data/prices.csv") as f:
        records = parse_csv(f, types=[str, float], has_header=False)

    with open("Data/prices.csv") as f:
        records = parse_csv(f, has_header=False)

    with open("Data/portfolio.dat") as f:
        records = parse_csv(f,
                            types=[str, int, float], delimiter=' ')

    with open("Data/portfolio.csv") as f:
        records = parse_csv(f, types=[str, int, float])

    with open("Data/missing.csv") as f:
        records = parse_csv(f, types=[str, int, float])

    with open("Data/portfolio.csv") as f:
        records = parse_csv("Data/portfolio.csv",
                            select=['name', 'shares'],
                            has_header=False)
