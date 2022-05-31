#!/usr/bin/python3

import ast
import sys


def multiply(*params):
    """
    Calculates the multiplication operation for the given expressions.
    :param : all parameters are expressions - each expression must be in the format of integer or a list
    :return: An Integer expression
    """
    r = 1
    for param in params:
        if type(param) == list:
            if param[0] == 'multiply':
                r = r * multiply(*param[1:])
            elif param[0] == 'add':
                r = r * add(*param[1:])
        else:
            r = r * int(param)
    return r


def add(*exprs):
    """
    Calculates the addition operation for the given expressions.
    :param : all parameters are expressions - each expression must be in the format of integer or a list
    :return: An Integer expression
    """
    s = 0
    for expr in exprs:
        if type(expr) == list:
            if expr[0] == 'add':
                s = s + add(*expr[1:])
            elif expr[0] == 'multiply':
                s = s + multiply(*expr[1:])
        elif type(expr) == int:
            s = s + int(expr)
    return s


def calulate(sexpr):
    """
    Determines which operation(addition or multiplication) that needs to be performed based on the given S-expression
    or its just a numeric expression
    :param : S-expression
    :return: An Integer expression
    """
    if sexpr[0] == 'multiply':
        return multiply(*sexpr[1:])
    elif sexpr[0] == 'add':
        return add(*sexpr[1:])


if __name__ == '__main__':
    # Check if
    if len(sys.argv) == 2:
        sexp = sys.argv[1]
        if sexp.isdigit():
            print(sexp)
        else:
            sexp = sexp.replace('(', '[').replace(')', ']').replace(' ', ',').replace('multiply', '"multiply"')\
                .replace('add','"add"')
            sext_in_pyt_lit = ast.literal_eval(sexp)
            print(calulate(sext_in_pyt_lit))
