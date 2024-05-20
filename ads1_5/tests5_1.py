''' Tests for lesson 5 task 1 solution. '''

import unittest
from random import randint
from parametrize import parametrize
from solution5_1 import Queue

class QueueTest(unittest.TestCase):
    ''' Tests for Queue class. '''
    def setUp(self) -> None:
        ''' Tests preparation. '''
        self.queue : Queue = Queue()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        del self.queue

    def test_size_on_empty_queue(self) -> None:
        ''' Tests size() for empty queue. Expected size = 0.'''
        self.assertEqual(self.queue.size(), 0)

    def test_dequeue_on_empty_queue(self) -> None:
        ''' Tests dequeue() on empty queue. Expected "None" returned. '''
        self.assertIsNone(self.queue.dequeue())

    def test_peek_on_empty_queue(self) -> None:
        ''' Tests peek() on empty queue. Expected "None" returned. '''
        self.assertIsNone(self.queue.peek())

    def test_enqueue_on_empty_queue(self) -> None:
        ''' Tests enqueue() on empty queue. Expected size = 1. '''
        self.queue.enqueue(0)
        self.assertEqual(self.queue.size(), 1)

    def test_peek_on_one_elem_queue(self) -> None:
        ''' Tests peek() on queue with one elem. Expected to return
            same value that was enqueued and size = 1 after operation. '''
        self.queue.enqueue(5)
        self.assertIs(self.queue.peek(), 5)
        self.assertEqual(self.queue.size(), 1)

    def test_dequeue_on_one_elem_queue(self) -> None:
        ''' Tests dequeue() on queue with one elem. Expected to return same
            value that was enqueued and that value must be removed from the queue. '''
        self.queue.enqueue(5)
        self.assertIs(self.queue.dequeue(), 5)
        self.assertEqual(self.queue.size(), 0)
        self.assertIsNone(self.queue.peek())

    def test_enqueue_on_one_elem_queue(self) -> None:
        ''' Tests enqueue() on queue with one elem. Expected size = 2 and
            enqueued value must go in tail. '''
        self.queue.enqueue(5)
        self.queue.enqueue(6)
        self.assertEqual(self.queue.size(), 2)
        self.assertIs(self.queue.peek(), 5)

    def test_enqueue_on_large_queue(self) -> None:
        ''' Tests enqueue() on large queue. Expected size growing by one 
            each time value is enqueued and value must go in tail. '''
        enqueue_times : int = 10000
        for i in range(enqueue_times):
            with self.subTest():
                self.queue.enqueue(i)
                self.assertEqual(self.queue.size(), i + 1)
                self.assertIs(self.queue.peek(), 0)

    def test_dequeue_on_large_queue(self) -> None:
        ''' Tests dequeue() on large queue. Expected size shrinking by one
            each time value is dequeued. Must return values exactly in
            order they were enqueued. Must return None when size = 0. '''
        initial_size : int = 10000
        for i in range(initial_size):
            self.queue.enqueue(i)
        self.assertEqual(self.queue.size(), initial_size)
        for i in range(initial_size):
            with self.subTest():
                self.assertEqual(self.queue.dequeue(), i)
                self.assertEqual(self.queue.size(), initial_size - i - 1)
        self.assertIsNone(self.queue.dequeue())
        self.assertEqual(self.queue.size(), 0)

    @parametrize('repeat_times', range(100))
    def test_large_random_queue(self, repeat_times) -> None:
        ''' Tests all operations on large queue with random values. '''
        initial_size : int = 10000
        current_size : int = initial_size
        operations_number : int = 10000
        for _ in range(initial_size):
            self.queue.enqueue(randint(-100, 100))
        self.assertEqual(self.queue.size(), initial_size)
        for i in range(operations_number):
            op : int = randint(1, 2)
            with self.subTest(i = i, op_code = op):
                if op == 1:
                    self.queue.enqueue(randint(-100, 100))
                    current_size += 1
                    self.assertEqual(self.queue.size(), current_size)
                    continue
                value = self.queue.peek() if current_size > 0 else None
                if op == 2:
                    current_size = max(current_size - 1, 0)
                if value is None:
                    self.assertIsNone(self.queue.dequeue())
                    self.assertEqual(self.queue.size(), current_size)
                    continue
                if value is not None:
                    self.assertIsNotNone(self.queue.dequeue())
                    self.assertEqual(self.queue.size(), current_size)
                    continue



unittest.main()
