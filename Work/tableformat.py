# tableformat.py


class FormatError(Exception):
    pass


class TableFormatter:
    def headings(self, headers):
        """Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """Emit a table in plain-text format.
    """
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end = ' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    """Output portfolio data in CSV format.
    """
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        res = []
        res.append('<tr>')
        for h in headers:
            res.append('<th>')
            res.append(h)
            res.append('</th>')
        res.append('</tr>')
        print(''.join(res))

    def row(self, rowdata):
        res = []
        res.append('<tr>')
        for d in rowdata:
            res.append('<td>')
            res.append(d)
            res.append('</td>')
        res.append('</tr>')
        print(''.join(res))


def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        # raise RuntimeError(f'Unknown format {fmt}')
        raise FormatError(f'Unknown table format {fmt}')


def print_table(portfolio, columns, formatter):
    formatter.headings(columns)
    for stock in portfolio:
        rowdata = [str(getattr(stock, column)) for column in columns]
        formatter.row(rowdata)
