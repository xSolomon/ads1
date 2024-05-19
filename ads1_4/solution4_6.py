''' Lesson 4 task 6 solution. '''

import operator
from typing import Callable
from solution4_1 import Stack

def eval_expression_in_postfix_form(expression_stack : Stack) -> int | None:
    ''' Evals expression in postfix form using two stacks.
        Allowed operations: + * =, where:
        = ends evaluation with its current result.
        Assumes that expression is correct. '''
    result_stack : Stack = Stack()
    operations : dict[str, Callable] = {
        '+': operator.add,
        '*': operator.mul,
    }
    token : str | int
    while token := expression_stack.pop():
        if token in operations:
            op : int = result_stack.pop()
            result_stack.push(operations[token](op, result_stack.pop()))
            continue
        if token == '=':
            return result_stack.pop()
        result_stack.push(token)
    return None
