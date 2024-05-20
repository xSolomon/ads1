''' Lesson 6 task 2 solution. '''

from solution6_1 import Deque

def is_palindrom(string : str) -> bool:
    ''' Determines whether given string is a palindrom.
        Does it by using Deque. '''
    deque : Deque = Deque()
    for c in string.lower():
        deque.addTail(c)
    while deque.size() > 1:
        if deque.removeFront() != deque.removeTail():
            return False
    return True
