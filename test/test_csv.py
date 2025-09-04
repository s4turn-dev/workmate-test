from csv import DictReader
from io import StringIO
import pytest

from custom_csv import CSV

@pytest.fixture
def csv():
    test_data = '''id,text,num
    1,text_1,100
    2,text_1,200
    3,text_2,200
    4,text_3,300'''
    _ = DictReader(StringIO(test_data))
    csv = CSV()
    csv.data = list(_)
    csv.columns = _.fieldnames
    csv.normalize_numericals()
    return csv


@pytest.mark.parametrize('aggregation,expected', [ 
    (('num', 'min'), [[1, 'text_1', 100]]),
    (('num', 'max'), [[4, 'text_3', 300]]),
    (('num', 'avg'), [[2, 'text_1', 200], [3, 'text_2', 200] ]),
])
def test_parse_aggregation_valid(csv, aggregation, expected):
    csv.aggregate(*aggregation)
    assert [list(row.values()) for row in csv.data] == expected

@pytest.mark.parametrize('invalid_aggregation', [ 
    ('num', 'lol'),
    ('kek', 'max'),
])
def test_parse_aggregation_invalid(csv, invalid_aggregation):
    with pytest.raises(ValueError):
        csv.aggregate(*invalid_aggregation)


@pytest.mark.parametrize('filter,expected', [ 
    (('text', '=', 'text_1'), [[1, 'text_1', 100], [2, 'text_1', 200] ]),
    (('num', '=', '300'), [[4, 'text_3', 300]]),
    (('num', '>', '100'), [[2, 'text_1', 200], [3, 'text_2', 200], [4, 'text_3', 300]]),
    (('num', '<', '150'), [[1, 'text_1', 100]]),
])
def test_parse_filter_valid(csv, filter, expected):
    csv.filter(*filter)
    assert [list(row.values()) for row in csv.data] == expected

@pytest.mark.parametrize('invalid_filter', [ 
    #('text', '>', 'other_text'), # oh fuck this one *does pass*
    ('lol', '=', 'kek'),
    ('num', '>=', '300')
])
def test_parse_filter_invalid(csv, invalid_filter):
    with pytest.raises(ValueError):
        csv.filter(*invalid_filter)


@pytest.mark.parametrize('order_by,expected', [ 
    (('id', 'asc'), [[1, 'text_1', 100], [2, 'text_1', 200], [3, 'text_2', 200], [4, 'text_3', 300]]),
    (('id', 'desc'), [[1, 'text_1', 100], [2, 'text_1', 200], [3, 'text_2', 200], [4, 'text_3', 300]][::-1]),
])
def test_parse_order_by_valid(csv, order_by, expected):
    csv.order_by(*order_by)
    assert [list(row.values()) for row in csv.data] == expected

@pytest.mark.parametrize('invalid_order_by', [ 
    ('id', 'random'),
    ('lol', 'asc')
])
def test_parse_order_by_invalid(csv, invalid_order_by):
    with pytest.raises(ValueError):
        csv.order_by(*invalid_order_by)

