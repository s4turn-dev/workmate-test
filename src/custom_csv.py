import csv
from typing import Self

from tabulate import tabulate


class CSV:
    def __init__(self, filename: str | None = None):
        self.data = []
        self.columns = []
        if filename:
            self.load_from_file(filename)

    def __repr__(self):
        return tabulate(self.data, headers={col: col for col in self.columns})

    def load_from_file(self, filename: str):
        with open(filename, 'r', encoding='utf=8', newline='') as file:
            reader = csv.DictReader(file)
            self.data = list(reader)
            self.columns = reader.fieldnames
        self.normalize_numericals()

    def normalize_numericals(self):
        # The only way I thought of
        num_keys = []
        for key, _ in self.data[0].items():
            try:
                float(self.data[0][key])
            except ValueError:
                pass
            else:
                num_keys.append(key)
        for i in range(len(self.data)):
            for key in num_keys:
                self.data[i][key] = float(self.data[i][key])

    @staticmethod
    def _validate_column(function):
        def inner(self, *args, **kwargs):
            column = kwargs.get('column') or (args[0] if args else None) # This looks ugly but I really kinda
                                                                         # want to keep the decorator as it is... 
            if column in self.columns:
                return function(self, *args, **kwargs)
            raise ValueError(f'{function.__name__}: Unknown column: {column}')
        return inner

    @_validate_column
    def aggregate(self, column: str, function: str) -> Self:
        all_nums = [row[column] for row in self.data]
        match function:
            case 'min':
                target = min(all_nums)
            case 'max':
                target = max(all_nums)
            case 'avg':
                try:
                    target = sum(all_nums) / len(all_nums)
                except ZeroDivisionError:
                    target = 1337
            case _:
                raise ValueError('aggregate: Unsupported function:', function)
        self.data = [row for row in self.data if row[column] == target]
        # Before even writing any code I decided I want to be able to chain commands,
        # akin to SQLAlchemy (Model.filter().first()...) – hence the self returns
        return self

    @_validate_column
    def filter(self, column: str, relation: str, value: str) -> Self:
        try:
            # I'm not sure how bad this is, given the type hint ^
            value = float(value)
        except ValueError:
            pass

        match relation:
            case '<':
                relation_check = lambda x,y: x<y
            case '>':
                relation_check = lambda x,y: x>y
            case '=':
                relation_check = lambda x,y: x==y
            case _:
                raise ValueError('filter: Unsupported relation:', relation)
        self.data = [row for row in self.data if relation_check(row[column], value)]
        return self

    @_validate_column
    def order_by(self, column: str, order: str) -> Self:
        order = order.lower()
        if order not in ('asc', 'desc'):
            raise ValueError(f'order_by: Unsupported option: {order}')
        self.data = sorted(self.data, key=lambda row: row[column], reverse=order=='desc')
        return self

