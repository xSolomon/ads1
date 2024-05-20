''' Tests for lesson 5 task 2 solution. '''

import unittest
from random import randint
from solution5_2 import rotate_queue, Queue

class RotateQueueTests(unittest.TestCase):
    ''' Tests for rotate_queue() function. '''
    def setUp(self) -> None:
        ''' Test preparation. '''
        self.queue = Queue()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        while self.queue.dequeue():
            continue
        del self.queue

    def test_on_empty_queue(self) -> None:
        ''' Test on empty queue. Tries to rotate negative, zero, positive number of times.
            Expected unchanged state. '''
        rotation_times_list : list[int] = [-5, 0, 5]
        for rotation_times in rotation_times_list:
            with self.subTest(rotation_times = rotation_times):
                rotate_queue(self.queue, rotation_times)
                self.assertEqual(self.queue.size(), 0)
                self.assertIsNone(self.queue.peek())

    def test_on_single_elem_queue(self) -> None:
        ''' Test on queue with only one elem. Expected unchanged state. '''
        rotation_times_list : list[int] = [-5, 0, 5]
        self.queue.enqueue(5)
        for rotation_times in rotation_times_list:
            with self.subTest(rotation_times = rotation_times):
                rotate_queue(self.queue, rotation_times)
                self.assertEqual(self.queue.size(), 1)
                self.assertEqual(self.queue.peek(), 5)

    def test_on_large_queue(self) -> None:
        ''' Test on large predefined queue. Random rotation number.
            Size of queue mustn't change. '''
        queue_size : int = 10000
        test_times : int = 100
        for i in range(queue_size):
            self.queue.enqueue(i)
        current_head_value : int = 0
        for i in range(test_times):
            rotation_times : int = randint(-queue_size, queue_size)
            with self.subTest(test_no = i, rotation_times = rotation_times):
                rotate_queue(self.queue, rotation_times)
                self.assertEqual(self.queue.size(), queue_size)
                if rotation_times >= 0:
                    current_head_value = (current_head_value + rotation_times) % queue_size
                self.assertEqual(self.queue.peek(), current_head_value)

unittest.main()
