from argparse import ArgumentParser, Namespace

import re

# TODO: Test


class CustomArgumentParser(ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_argument('--file', required=True)
        self.add_argument('--aggregation')
        self.add_argument('--where')
        self.add_argument('--order-by')

    def parse_args(self, *args, **kwargs) -> Namespace:
        self.args = super().parse_args(*args, **kwargs)
        return self.args

    # Я попробовал наверное 5 разных вариантов, каждый из которых в сущности
    # подразумевал повторение одного и того же кода с незначительными изменениями
    # для каждой команды, и решил, что представленный ниже – наиболее удачный

    def _parse_command(self, regex: str, input: str) -> tuple | None:
        match = re.search(regex, input)
        return match.groups() if match else None

    # Принимать сырое значение как аргумент (input: str)?
    # Не прнимать никаких значений, работать с self.args?

    # Разделять ли сырые аргументы и распарсенные (сейчас)
    # или переписывать вторые первыми (иметь один self.args)?
    
    def parse_aggregation(self) -> tuple | None:
        if self.args.aggregation is not None:
            re = r'^(.*?)=(min|max|avg)$'
            args = self._parse_command(re, self.args.aggregation)
            if args:
                self.args.aggregation = args
                return self.args.aggregation
            raise ValueError('aggregation: Not found:', self.args.aggregation)

    def parse_filter(self) -> tuple | None:
        if self.args.where is not None:
            re = r'^(.*?)([<>=])(.*?)$'
            args = self._parse_command(re, self.args.where)
            if args:
                self.args.where = args
                return self.args.where
            raise ValueError('filter: Not found:', self.args.where)

    def parse_order_by(self) -> tuple | None:
        if self.args.order_by is not None:
            re = r'^(.*?)=(asc|desc)$'
            args = self._parse_command(re, self.args.order_by)
            if args:
                self.args.order_by = args
                return self.args.order_by
            raise ValueError('order by: Not found:', self.args.order_by)



