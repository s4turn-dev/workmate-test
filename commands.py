# Проблема: аргументы методов класса CSV нужно иметь в синхронизации с typehint-ами
# методов класса CommandParser. Меняется один – нужно менять другой

# [AI SUGGESTED] Решение: напилить middle-layer объектов, к которым будут обращаться оба класса

from dataclasses import dataclass

from typing import Literal


@dataclass
class AggregationCommand:
    column: str
    function: Literal['min', 'max', 'avg']


@dataclass
class FilterCommand:
    column: str
    relation: Literal['>', '<', '=']
    value: str | float


@dataclass
class OrderByCommand:
    column: str
    order: Literal['asc', 'desc']

