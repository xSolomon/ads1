''' Lesson 5 task 4 solution. '''

from stack import Stack

class Queue:
    ''' Represents FIFO queue implemented via two stacks. '''
    def __init__(self):
        self.in_stack : Stack = Stack()
        self.out_stack : Stack = Stack()

    def enqueue(self, item) -> None:
        ''' Insert item in the tail of queue. '''
        self.in_stack.push(item)

    def dequeue(self):
        ''' Removes and returns item from queue head. '''
        if self.out_stack.size() > 0:
            return self.out_stack.pop()
        while self.in_stack.size() > 0:
            self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        ''' Return queue head without removing it. '''
        if self.out_stack.size() > 0:
            return self.out_stack.peek()
        while self.in_stack.size() > 0:
            self.out_stack.push(self.in_stack.pop())
        return self.out_stack.peek()

    def size(self) -> int:
        ''' Returns current queue size. '''
        return self.in_stack.size() + self.out_stack.size()
