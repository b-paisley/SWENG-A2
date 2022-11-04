import unittest
import math
from calc import is_num
from calc import to_list
from calc import func
from calc import operator
from calc import find_bracket
from calc import calc


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


def test_is_num():
    assert is_num("300") == True
    assert is_num("?") == False


def test_to_list():
    assert to_list("50 * 7 - 3") == [50, "*", 7, "-", 3]


def test_func():
    assert func(['exp', 5], 'exp') == [math.exp(5)]
    assert func(['log', 8], 'log') == [math.log(8)]


def test_operator():
    assert operator([5, '*', 8], '*', '/') == [40]
    assert operator([6, '-', 3], '+', '-') == [3]


def test_find_bracket():
    assert find_bracket(0,['(', 5, '*', 6, '+', '(', 2, '+', 1, ')', ')'])==10


def test_calc():
    result = to_list('3+5*exp(4.2)/(5+7)')
    assert round(calc(result),3)==30.786


if __name__ == '__main__':
    unittest.main()
