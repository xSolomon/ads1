''' Stack realisation on default python list (dynamic ary). '''

class Stack:
    ''' Represents stack (on python list). '''
    def __init__(self):
        self.stack : list = []

    def size(self) -> int:
        ''' Return current stack length. '''
        return len(self.stack)

    def pop(self):
        ''' Pop and return stack head. Returns none if stack is empty. '''
        return self.stack.pop() if len(self.stack) > 0 else None

    def push(self, value):
        ''' Add value in stack head. '''
        self.stack.append(value)

    def peek(self):
        ''' Return stack head without removing it. '''
        return self.stack[-1] if len(self.stack) > 0 else None





