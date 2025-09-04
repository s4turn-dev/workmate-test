from argparse import ArgumentParser
import pytest

from command_parser import CommandParser

@pytest.fixture
def argprs():
    argprs = ArgumentParser()
    argprs.add_argument('--aggregation')
    argprs.add_argument('--where')
    argprs.add_argument('--order-by')
    return argprs


@pytest.mark.parametrize('aggregation,expected', [ 
    ('column=min', ('column', 'min')),
    ('column=max', ('column', 'max')),
    ('column=avg', ('column', 'avg')),
    ('column==min', ('column=', 'min')),
    ('col.umn=avg', ('col.umn', 'avg')),
])
def test_parse_aggregation_valid(argprs, aggregation, expected):
    raw_args = argprs.parse_args(['--aggregation', aggregation])
    cmdprs = CommandParser(raw_args)
    assert cmdprs.aggregation == expected

@pytest.mark.parametrize('invalid_str', [
    'column min',
    'column = max',
    'column=avg ',
    'column=bob',
    'column',
    ''
])
def test_parse_aggregation_invalid(argprs, invalid_str):
    raw_args = argprs.parse_args(['--aggregation', invalid_str])
    with pytest.raises(ValueError):
        CommandParser(raw_args)


# Filter
@pytest.mark.parametrize('filter,expected', [ 
    ('column=value', ('column', '=', 'value')),
    ('column>value', ('column', '>', 'value')),
    ('column<value', ('column', '<', 'value')),
    ('column = value', ('column', '=', 'value')),
    ('column==value', ('column', '=', '=value')),
    ('column>=value', ('column', '>', '=value')), # !!!
    ('col.umn=avg', ('col.umn', '=', 'avg')),
])
def test_parse_filter_valid(argprs, filter, expected):
    raw_args = argprs.parse_args(['--where', filter])
    cmdprs = CommandParser(raw_args)
    assert cmdprs.filter == expected

@pytest.mark.parametrize('invalid_str', [
    'column value',
    'column',
    ''
])
def test_parse_filter_invalid(argprs, invalid_str):
    raw_args = argprs.parse_args(['--where', invalid_str])
    with pytest.raises(ValueError):
        CommandParser(raw_args)


# Order By
@pytest.mark.parametrize('order_by,expected', [ 
    ('column=asc', ('column', 'asc')),
    ('column=desc', ('column', 'desc')),
    ('column  =desc', ('column  ', 'desc')),
])
def test_parse_order_by_valid(argprs, order_by, expected):
    raw_args = argprs.parse_args(['--order-by', order_by])
    cmdprs = CommandParser(raw_args)
    assert cmdprs.order_by == expected

@pytest.mark.parametrize('invalid_str', [
    'column asc',
    'column=dsc',
    'column',
    ''
])
def test_parse_order_by_invalid(argprs, invalid_str):
    raw_args = argprs.parse_args(['--order-by', invalid_str])
    with pytest.raises(ValueError):
        CommandParser(raw_args)

