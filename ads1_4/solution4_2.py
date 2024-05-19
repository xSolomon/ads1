''' Stack realisation using list head instead of tail.
    Uses a bit extended doubly linked circular list with one dummy node
    from lesson 2 task 10 solution for O(1) operations complexity. '''

from linked_list import LinkedList, Node

class Stack:
    ''' Represents stack (on LinkedList). '''
    def __init__(self):
        self.stack : LinkedList = LinkedList()

    def size(self) -> int:
        ''' Return current stack length. '''
        return len(self.stack)

    def pop(self):
        ''' Pop and return stack head. Returns none if stack is empty. '''
        if len(self.stack) == 0:
            return None
        item = self.stack.get_head().value
        self.stack.delete(self.stack.get_head().value)
        return item

    def push(self, value):
        ''' Add value in stack head. '''
        self.stack.insert(Node(value))

    def peek(self):
        ''' Return stack head without removing it. '''
        return None if len(self.stack) == 0 else self.stack.get_head().value
