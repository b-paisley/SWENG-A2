import math
from calc import is_num
from calc import to_list
from calc import func
from calc import operator
from calc import find_bracket
from calc import calc


def test_is_num():
    assert is_num("300")
    assert not is_num("?")


def test_to_list():
    assert to_list("50*7-3") == [50, '*', 7, '-', 3]
    assert to_list("50 - 7 * 3") == [50, '-', 7, '*', 3]


def test_func():
    assert func(['exp', 5.0], 'exp') == [math.exp(5)]
    assert func(['log', 8.0], 'log') == [math.log(8)]


def test_operator():
    assert operator([5.0, '*', 8.0], '*', '/') == [40]
    assert operator([6.0, '-', 3.0], '+', '-') == [3]


def test_find_bracket():
    assert find_bracket(0, ['(', 5.0, '*', 6.0, '+', '(', 2.0, '+', 1.0, ')', ')']) == 10.0


def test_calc():
    result = to_list('3+5*exp(4.2)/(5+7)')
    assert round(calc(result), 3) == 30.786
