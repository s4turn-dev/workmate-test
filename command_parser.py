from argparse import Namespace
import re

import commands


class CommandParser:
    def __init__(self, raw_args: Namespace):
        self._raw = raw_args
        self.aggregation = self.parse_aggregation()
        self.filter = self.parse_filter()
        self.order_by = self.parse_order_by()

    # Я попробовал наверное 5 разных вариантов, каждый из которых в сущности
    # подразумевал повторение одного и того же кода с незначительными изменениями
    # для каждой команды, и решил, что представленный ниже – наиболее удачный
    def __repr__(self):
        return f'{self.__class__.__name__}({self.aggregation=}, {self.filter=}, {self.order_by=})'

    def _parse_command(self, regex: str, input: str) -> tuple | None:
        match = re.search(regex, input)
        return match.groups() if match else None
    
    def parse_aggregation(self) -> commands.AggregationCommand | None:
        if self._raw.aggregation is not None:
            re = r'^(.*?)=(min|max|avg)$'
            args = self._parse_command(re, self._raw.aggregation)
            if args:
                return commands.AggregationCommand(*args)
            raise ValueError('aggregation: Not found:', self._raw.aggregation)

    def parse_filter(self) -> commands.FilterCommand | None:
        if self._raw.where is not None:
            re = r'^(.*?)([<>=])(.*?)$'
            args = self._parse_command(re, self._raw.where)
            if args:
                return commands.FilterCommand(*args)
            raise ValueError('filter: Not found:', self._raw.filter)

    def parse_order_by(self) -> commands.OrderByCommand | None:
        if self._raw.order_by is not None:
            re = r'^(.*?)=(asc|desc)$'
            args = self._parse_command(re, self._raw.order_by)
            if args:
                return commands.OrderByCommand(*args)
            raise ValueError('order by: Not found:', self._raw.order_by)

