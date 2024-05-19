''' Tests for stack size(), pop(), push() and peek() functions. '''

import unittest
from random import randint
from parametrize import parametrize
from solution4_2 import Stack

class StackTest(unittest.TestCase):
    ''' Tests for Stack class. '''
    def setUp(self) -> None:
        ''' Tests preparation. '''
        self.stack : Stack = Stack()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        del self.stack

    def test_size_on_empty_stack(self) -> None:
        ''' Tests size() for empty stack. Expected size = 0.'''
        self.assertEqual(self.stack.size(), 0)

    def test_pop_on_empty_stack(self) -> None:
        ''' Tests pop() on empty stack. Expected "None" returned. '''
        self.assertIsNone(self.stack.pop())

    def test_peek_on_empty_stack(self) -> None:
        ''' Tests peek() on empty stack. Expected "None" returned. '''
        self.assertIsNone(self.stack.peek())

    def test_push_on_empty_stack(self) -> None:
        ''' Tests push() on empty stack. Expected size = 1. '''
        self.stack.push(0)
        self.assertEqual(self.stack.size(), 1)

    def test_peek_on_one_elem_stack(self) -> None:
        ''' Tests peek() on stack with one elem. Expected to return
            same value that was pushed and size = 1 after operation. '''
        self.stack.push(5)
        self.assertIs(self.stack.peek(), 5)
        self.assertEqual(self.stack.size(), 1)

    def test_pop_on_one_elem_stack(self) -> None:
        ''' Tests pop() on stack with one elem. Expected to return same
            value that was pushed and that value must be removed from the stack. '''
        self.stack.push(5)
        self.assertIs(self.stack.pop(), 5)
        self.assertEqual(self.stack.size(), 0)
        self.assertIsNone(self.stack.peek())

    def test_push_on_one_elem_stack(self) -> None:
        ''' Tests push() on stack with one elem. Expected size = 2 and
            pushed value to be new stack head. '''
        self.stack.push(5)
        self.stack.push(6)
        self.assertEqual(self.stack.size(), 2)
        self.assertIs(self.stack.peek(), 6)

    def test_push_on_large_stack(self) -> None:
        ''' Tests push() on large stack. Expected size growing by one 
            each time value is pushed and value must be new stack head. '''
        push_times : int = 1000
        for i in range(push_times):
            with self.subTest():
                self.stack.push(i)
                self.assertEqual(self.stack.size(), i + 1)
                self.assertIs(self.stack.peek(), i)

    def test_pop_on_large_stack(self) -> None:
        ''' Tests pop() on large stack. Expected size shrinking by one
            each time value is popped. Must return values exactly in reverse
            order they were pushed. Must return None when size = 0. '''
        initial_size : int = 1000
        for i in range(initial_size):
            self.stack.push(i)
        self.assertEqual(self.stack.size(), initial_size)
        for i in reversed(range(initial_size)):
            with self.subTest():
                self.assertEqual(self.stack.pop(), i)
                self.assertEqual(self.stack.size(), i)
        self.assertIsNone(self.stack.pop())
        self.assertEqual(self.stack.size(), 0)

    @parametrize('repeat_times', range(100))
    def test_large_random_stack(self, repeat_times) -> None:
        ''' Tests all operations on large stack with random values. '''
        initial_size : int = 1000
        current_size : int = initial_size
        operations_number : int = 1000
        for _ in range(initial_size):
            self.stack.push(randint(-100, 100))
        self.assertEqual(self.stack.size(), initial_size)
        for i in range(operations_number):
            op : int = randint(1, 2)
            with self.subTest(i = i, op_code = op):
                if op == 1:
                    self.stack.push(randint(-100, 100))
                    current_size += 1
                    self.assertEqual(self.stack.size(), current_size)
                    continue
                value = self.stack.peek() if current_size > 0 else None
                if op == 2:
                    current_size = max(current_size - 1, 0)
                if value is None:
                    self.assertIsNone(self.stack.pop())
                    self.assertEqual(self.stack.size(), current_size)
                    continue
                if value is not None:
                    self.assertIsNotNone(self.stack.pop())
                    self.assertEqual(self.stack.size(), current_size)
                    continue



unittest.main()
