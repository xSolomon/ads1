''' Solution 4_5 '''

from solution4_1 import Stack

def is_parentheses_sequence_balanced(string_of_parentheses : str) -> bool:
    ''' Checks if parentheses in given string are balanced:
        For every "(" there must be ")" and vice versa. '''
    stack : Stack = Stack()
    for c in string_of_parentheses:
        if c == '(':
            stack.push(c)
            continue
        if c == ')' and stack.size() > 0:
            stack.pop()
            continue
        if c == ')' and stack.size() == 0:
            return False
    return stack.size() == 0
