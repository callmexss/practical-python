# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename,
              select=[],
              types=[],
              has_header=True,
              delimiter=',',
              silence_errors=True):
    """Parse a CSV file into a list of records.
    """
    if select and not has_header:
        raise RuntimeError("select argument requires column headers")
    with open(filename) as f:
        records = []
        rows = csv.reader(f, delimiter=delimiter)
        if not has_header:
            for i, row in enumerate(rows, start=1):
                if not row:
                    continue
                if types:
                    try:
                        records.append(tuple(
                            [func(val) for func, val in zip(types, row)]))
                    except ValueError as err:
                        if not silence_errors:
                            print(f"Row {i}: Couldn't convert {row}")
                            print(f"Row {i}: Reason {err}")
                else:
                    records.append(tuple(row))
            return records

        header = next(rows)
        for i, row in enumerate(rows, start=1):
            if not row:
                continue
            try:
                if select:
                    indices = [header.index(each) for each in select]
                    header = [header[i] for i in indices]
                    row = [row[i] for i in indices]
                if types:
                    row = [func(val) for func, val in zip(types, row)]
            except ValueError as err:
                if not silence_errors:
                    print(f"Row {i}: Couldn't convert {row}")
                    print(f"Row {i}: Reason {err}")
            record = dict(zip(header, row))
            records.append(record)
    return records


if __name__ == "__main__":
    records = parse_csv("Data/portfolio.csv")
    records = parse_csv("Data/portfolio.csv", select=['name', 'shares'])
    records = parse_csv("Data/portfolio.csv", types=[str, int, float])
    records = parse_csv("Data/portfolio.csv",
                        select=['name', 'price'],
                        types=[str, float])
    records = parse_csv("Data/prices.csv", types=[str, float], has_header=False)
    records = parse_csv("Data/portfolio.dat",
                        types=[str, int, float], delimiter=' ')
    records = parse_csv("Data/portfolio.csv", types=[str, int, float])
    records = parse_csv("Data/missing.csv", types=[str, int, float])
    records = parse_csv("Data/portfolio.csv",
                        select=['name', 'shares'],
                        has_header=False)
    print(records)
