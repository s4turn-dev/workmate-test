# Проблема: аргументы методов класса CSV нужно иметь в синхронизации с typehint-ами
# методов класса CommandParser. Меняется один – нужно менять другой

# [AI SUGGESTED] Решение: напилить middle-layer объектов, к которым будут обращаться оба класса

from dataclasses import dataclass
from typing import Literal


class Repr:
    def __repr__(self):
        args = ', '.join(f'{arg}={value!r}' for arg, value in self.__dict__.items())
        return f'{self.__class__.__name__}({args})'


@dataclass
class AggregationCommand(Repr):
    column: str
    function: Literal['min', 'max', 'avg']


@dataclass
class FilterCommand(Repr):
    column: str
    relation: Literal['>', '<', '=']
    value: str | float


@dataclass
class OrderByCommand(Repr):
    column: str
    order: Literal['asc', 'desc']

