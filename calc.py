import re
import math

operators = ['+', '-', '*', '/', '^', 'exp', 'log', '(', ')']


def is_num(a: str) -> bool:
    """
    It identifies if an input string is number or not

    :param a: str
    :type a: str
    :return: A boolean value.
    """
    return re.match(r"\d*\.?\d+", a) is not None


def to_list(a: str) -> list:
    """
    It takes a string, strips it of whitespace, and then uses a regular expression to find all the numbers and
    operators in the string, and returns a list of those numbers and operators

    :param a: str - the string to be converted to a list
    :type a: str
    :return: A list of the numbers and operators in the string
    """
    a = a.strip()
    a.replace(' ', '')
    rst = []
    for matches in re.finditer(r"[+\-*^/()]|(exp)|(log)|(\d*\.?\d+)|.", a):
        if matches:
            item = matches[0]
            if not is_num(item) and item not in operators:
                raise Exception(f"{item} is invalid input")
            rst.append(item)
    for i in range(len(rst)):
        if is_num(rst[i]):
            rst[i] = float(rst[i])
    return rst


def func(list_in: list, func_in: str):
    """
    takes in a list and a function, the function can be exp or log
    calculate the function in the list and return the list

    :param list_in: the list of numbers and operators
    :type list_in: list
    :param func_in: the function you want to apply
    :type func_in: str
    :return: A list of numbers and operators after processing.
    """
    list_local = list_in
    while func_in in list_local:
        func_index = list_local.index(func_in)
        num_index = func_index + 1
        num = list_local[num_index]
        if type(num) != float:
            raise Exception('invalid input')
        head = list_local[:func_index]
        body = 0.0
        if func_in == 'exp':
            body = math.exp(num)
        if func_in == 'log':
            body = math.log(num)
        head.append(body)
        tail = list_local[num_index+1:]
        list_local = head + tail
    return list_local


def operator(list_in: list, op1: str, op2: str):
    """
    It takes a list and two operators op1 and op2 of same priority. For example: op1, op2 = '+', '-'
    Do op1 and op2 on the input list, then return the list.

    :param list_in: list
    :type list_in: list
    :param op1: the first operator to look for
    :type op1: str
    :param op2: the second operator to look for
    :type op2: str
    :return: the list with the operation performed on the list_in.
    """
    list_local = list_in

    while op1 in list_local or op2 in list_local:
        if op1 not in list_local:
            idx_op = list_local.index(op2)
            op = op2
        elif op2 not in list_local:
            idx_op = list_local.index(op1)
            op = op1
        elif list_local.index(op1) < list_local.index(op2):
            idx_op = list_local.index(op1)
            op = op1
        else:
            idx_op = list_local.index(op2)
            op = op2

        num1_idx = idx_op-1
        num2_idx = idx_op+1
        num1 = list_local[num1_idx]
        num2 = list_local[num2_idx]
        if type(num1) != float or type(num2) != float:
            raise Exception(f'must have two nums for doing {op}')
        head = list_local[:num1_idx]
        body = 0.0
        if op == '+':
            body = num1 + num2
        if op == '-':
            body = num1 - num2
        if op == '*':
            body = num1 * num2
        if op == '/':
            body = num1 / num2
        if op == '^':
            body = num1 ** num2
        head.append(body)
        tail = list_local[num2_idx+1:]
        list_local = head + tail
    return list_local


def find_bracket(index: int, list_in: list):
    """
    It finds the index of the closing bracket of the opening bracket at index

    :param index: the index of the opening bracket
    :type index: int
    :param list_in: the list of tokens
    :type list_in: list
    :return: The index of the closing bracket
    """
    count = 1
    for i in range(index+1, len(list_in)):
        if list_in[i] == '(':
            count += 1
        if list_in[i] == ')':
            count -= 1
            if count == 0:
                return i
    raise Exception('brackets are not closed')


def calc(list_in: list):
    """
    It takes a list of numbers and operators, and returns the result of the calculation.

    :param list_in: the list of the input
    :type list_in: list
    :return: The result of the calculation.
    """
    list_local = list_in

    while '(' in list_local:                             # get rid of all the brackets
        start = list_local.index('(')
        end = find_bracket(start, list_local)             # get the index of the
        head = list_local[:start]
        body = list_local[start+1:end]
        head.append(calc(body))
        tail = list_local[end+1:]
        list_local = head + tail
    if ')' in list_local:
        raise Exception('() is not balanced')
    list_local = func(list_local, 'log')
    list_local = func(list_local, 'exp')
    list_local = operator(list_local, '^', '~')
    list_local = operator(list_local, '*', '/')
    list_local = operator(list_local, '+', '-')
    if len(list_local) == 1:
        if type(list_local[0]) == float:
            return list_local[0]
        else:
            raise Exception("invalid input")


if __name__ == "__main__":
    result = to_list('3+5*exp(4.2)/(5+7)')
    try:
        print(round(calc(result), 3))
    except Exception as err:
        print(err)
