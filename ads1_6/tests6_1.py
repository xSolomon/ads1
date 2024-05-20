''' Tests for lesson 6 task 1 solution. '''

import unittest
from random import randint, choice
from parametrize import parametrize
from solution6_1 import Deque

class DequeTests(unittest.TestCase):
    ''' Tests addFront, addTail, removeFront, removeTail, peekFront,
        peekTail and size functions from Deque class. '''
    def setUp(self) -> None:
        ''' Test preparation. '''
        self.deque : Deque = Deque()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        del self.deque

    def test_size_on_empty_deque(self) -> None:
        ''' Tests size() on empty deque. Expected size = 0. '''
        self.assertEqual(self.deque.size(), 0)

    def test_peek_on_empty_deque(self) -> None:
        ''' Tests peekFront() and peekTail() on empty deque.
            Expected "None" return result and size unchanged. '''
        self.assertIsNone(self.deque.peekFront())
        self.assertEqual(self.deque.size(), 0)
        self.assertIsNone(self.deque.peekTail())
        self.assertEqual(self.deque.size(), 0)

    def test_remove_on_empty_deque(self) -> None:
        ''' Tests removeFront() and removeTail() on empty deque.
            Expected "None" return result, corresponding peek method
            must return "None" and size unchanged. '''
        self.assertIsNone(self.deque.removeFront())
        self.assertIsNone(self.deque.peekFront())
        self.assertIsNone(self.deque.peekTail())
        self.assertEqual(self.deque.size(), 0)
        self.assertIsNone(self.deque.removeTail())
        self.assertIsNone(self.deque.peekFront())
        self.assertIsNone(self.deque.peekTail())
        self.assertEqual(self.deque.size(), 0)

    def test_add_front_on_empty_deque(self) -> None:
        ''' Tests addFront() and on empty deque. Expected size = 1,
            peekTail() and peekFront() to return same value that was added. '''
        self.deque.addFront(5)
        self.assertEqual(self.deque.peekFront(), 5)
        self.assertEqual(self.deque.peekTail(), 5)
        self.assertEqual(self.deque.size(), 1)

    def test_add_tail_on_empty_deque(self) -> None:
        ''' Tests addTail() and on empty deque. Expected size = 1,
            peekTail() and peekFront() to return same value that was added. '''
        self.deque.addTail(5)
        self.assertEqual(self.deque.peekFront(), 5)
        self.assertEqual(self.deque.peekTail(), 5)
        self.assertEqual(self.deque.size(), 1)

    def test_remove_on_single_elem_deque(self) -> None:
        ''' Tests removeFront() and removeTail() on deque with one elem.
            Expected size = 0, peekFront() and peekTail() to return "None". '''
        for i in range(2):
            self.deque.addFront(5)
            with self.subTest():
                if i == 0:
                    self.deque.removeFront()
                if i == 1:
                    self.deque.removeTail()
                self.assertIsNone(self.deque.removeTail())
                self.assertIsNone(self.deque.peekTail())
                self.assertEqual(self.deque.size(), 0)

    def test_add_front_on_single_elem_deque(self) -> None:
        ''' Tests addFront() on deque with one elem.
            Expected size = 2, peekFront() to return added value. '''
        self.deque.addFront(5)
        self.deque.addFront(10)
        self.assertEqual(self.deque.peekFront(), 10)
        self.assertEqual(self.deque.size(), 2)

    def test_add_tail_on_single_elem_deque(self) -> None:
        ''' Tests addTail() on deque with one elem.
            Expected size = 2, peekTail() to return added value. '''
        self.deque.addFront(5)
        self.deque.addTail(10)
        self.assertEqual(self.deque.peekTail(), 10)
        self.assertEqual(self.deque.size(), 2)

    def test_peek_on_two_elem_deque(self) -> None:
        ''' Tests peekFront() and peekTail() on deque with two elems.
            Expected size = 2 and each method must return corresponding value. '''
        self.deque.addFront(5)
        self.deque.addFront(10)
        self.assertEqual(self.deque.peekFront(), 10)
        self.assertEqual(self.deque.peekTail(), 5)
        self.assertEqual(self.deque.size(), 2)

    def test_remove_front_on_two_elem_deque(self) -> None:
        ''' Tests removeFront() on deque with two elems. Expected size = 1,
        returned value must be from head, peekFront() and peekTail() to return same value. '''
        self.deque.addFront(5)
        self.deque.addFront(10)
        self.assertEqual(self.deque.removeFront(), 10)
        self.assertEqual(self.deque.peekFront(), 5)
        self.assertEqual(self.deque.peekTail(), 5)
        self.assertEqual(self.deque.size(), 1)

    def test_remove_tail_on_two_elem_deque(self) -> None:
        ''' Tests removeTail() on deque with two elems. Expected size = 1,
        returned value must be from tail, peekFront() and peekTail() to return same value. '''
        self.deque.addFront(5)
        self.deque.addFront(10)
        self.assertEqual(self.deque.removeTail(), 5)
        self.assertEqual(self.deque.peekFront(), 10)
        self.assertEqual(self.deque.peekTail(), 10)
        self.assertEqual(self.deque.size(), 1)

    def test_add_on_large_random_deque(self) -> None:
        ''' Tests addFront() and addTail() by creating large deque with random values.
            Expected size growing by 1 after each adding, and corresponding peek method must
            return value that was added (other peek method should return unchanged value). '''
        add_times : int = 10000
        add_in_tail : bool
        head_value : int = None
        tail_value : int = None
        add_value : int
        for i in range(add_times):
            add_in_tail = choice([True, False])
            add_value = randint(-100, 100)
            with self.subTest(i = i, add_in_tail = add_in_tail,
                head = head_value, tail = tail_value, adding = add_value):
                if i == 0:
                    head_value = add_value
                    tail_value = add_value
                    self.deque.addFront(add_value)
                if i != 0 and not add_in_tail:
                    self.deque.addFront(add_value)
                    head_value = add_value
                if i != 0 and add_in_tail:
                    self.deque.addTail(add_value)
                    tail_value = add_value
                self.assertEqual(self.deque.peekFront(), head_value)
                self.assertEqual(self.deque.peekTail(), tail_value)
                self.assertEqual(self.deque.size(), i + 1)

    def test_remove_on_large_predefined_deque(self) -> None:
        ''' Tests removeFront() and removeTail() by creating large deque with predefined values.
            Expected size shrinking by 1 after each adding, and corresponding peek method must
            return new head/tail value (other peek method should return unchanged value). '''
        initial_deque_size : int = 10000
        for i in range(initial_deque_size):
            self.deque.addTail(i)
        head_value : int = 0
        tail_value : int = initial_deque_size - 1
        remove_from_tail : bool
        current_deque_size : int = initial_deque_size
        for i in range(initial_deque_size):
            remove_from_tail = choice([True, False])
            with self.subTest(i = i, removeTail = remove_from_tail,
                head = head_value, tail = tail_value):
                if not remove_from_tail:
                    self.assertEqual(self.deque.removeFront(), head_value)
                    head_value += 1
                if remove_from_tail:
                    self.assertEqual(self.deque.removeTail(), tail_value)
                    tail_value -= 1
                current_deque_size -= 1
                self.assertEqual(self.deque.size(), current_deque_size)
                if current_deque_size == 0:
                    self.assertIsNone(self.deque.peekFront())
                    self.assertIsNone(self.deque.peekTail())
                    continue
                self.assertEqual(self.deque.peekFront(), head_value)
                self.assertEqual(self.deque.peekTail(), tail_value)

    def test_predefined_operation_set_with_predefined_values_on_single_elem_deque(self) -> None:
        ''' Tests operation sequence: addFront(), addFront(), removeTail()
            on predefined values and deque with one elem. '''
        self.deque.addTail(1)
        self.deque.addFront(5)
        self.deque.addFront(6)
        self.assertEqual(self.deque.removeTail(), 1)
        self.assertEqual(self.deque.peekFront(), 6)
        self.assertEqual(self.deque.peekTail(), 5)

    @parametrize('repeat_times', range(100))
    def test_on_large_random_deque(self, repeat_times : int) -> None:
        ''' Tests remove and add functions on large deck with random values.
            After each add/remove, size must grow/shrink by one (except when
            removing from empty deque, size remain same).
            For add, corresponding peek method must return same value that was added
            (other must return unchanched value).
            For remove, corresponding peek method must return changed value (other must
            return same value that was before operation). '''
        initial_deque_size : int = 100
        operations_number : int = 10000
        for _ in range(initial_deque_size):
            self.deque.addTail(randint(-100, 100))
        current_deque_size : int = initial_deque_size
        head_value : int = self.deque.peekFront()
        tail_value : int = self.deque.peekTail()
        value : int = None
        for i in range(operations_number):
            head_value = self.deque.peekFront()
            tail_value = self.deque.peekTail()
            perform_add : bool = choice([True, False])
            perform_on_tail : bool = choice([True, False])
            value = randint(-100, 100)
            with self.subTest(op_no = i + 1, deque_size = current_deque_size,
                is_performing_add = perform_add, is_performing_on_tail = perform_on_tail):
                if current_deque_size > 0 and perform_add and not perform_on_tail:
                    head_value = value
                    current_deque_size += 1
                    self.deque.addFront(value)
                    self.assertEqual(self.deque.size(), current_deque_size)
                    self.assertEqual(self.deque.peekFront(), head_value)
                    self.assertEqual(self.deque.peekTail(), tail_value)
                    continue
                if current_deque_size > 0 and perform_add and perform_on_tail:
                    tail_value = value
                    current_deque_size += 1
                    self.deque.addTail(value)
                    self.assertEqual(self.deque.size(), current_deque_size)
                    self.assertEqual(self.deque.peekFront(), head_value)
                    self.assertEqual(self.deque.peekTail(), tail_value)
                    continue
                if current_deque_size > 1 and not perform_add and not perform_on_tail:
                    current_deque_size -= 1
                    self.assertEqual(self.deque.removeFront(), head_value)
                    self.assertEqual(self.deque.size(), current_deque_size)
                    self.assertEqual(self.deque.peekTail(), tail_value)
                    continue
                if current_deque_size > 1 and not perform_add and perform_on_tail:
                    current_deque_size -= 1
                    self.assertEqual(self.deque.removeTail(), tail_value)
                    self.assertEqual(self.deque.size(), current_deque_size)
                    self.assertEqual(self.deque.peekFront(), head_value)
                    continue
                if current_deque_size == 1 and not perform_add and not perform_on_tail:
                    current_deque_size -= 1
                    self.assertEqual(self.deque.removeFront(), head_value)
                    head_value = tail_value = None
                    self.assertEqual(self.deque.size(), current_deque_size)
                    self.assertEqual(self.deque.peekTail(), tail_value)
                    continue
                if current_deque_size == 1 and not perform_add and perform_on_tail:
                    current_deque_size -= 1
                    self.assertEqual(self.deque.removeTail(), tail_value)
                    head_value = tail_value = None
                    self.assertEqual(self.deque.size(), current_deque_size)
                    self.assertEqual(self.deque.peekFront(), head_value)
                    continue
                if current_deque_size == 0 and not perform_add and not perform_on_tail:
                    self.assertIsNone(self.deque.removeFront())
                    self.assertEqual(self.deque.size(), current_deque_size)
                    self.assertIsNone(self.deque.peekFront())
                    self.assertIsNone(self.deque.peekTail())
                    continue
                if current_deque_size == 0 and not perform_add and perform_on_tail:
                    self.assertIsNone(self.deque.removeTail())
                    self.assertEqual(self.deque.size(), current_deque_size)
                    self.assertIsNone(self.deque.peekFront())
                    self.assertIsNone(self.deque.peekTail())
                    continue
                if current_deque_size == 0 and perform_add and not perform_on_tail:
                    head_value = tail_value = value
                    current_deque_size += 1
                    self.deque.addFront(value)
                    self.assertEqual(self.deque.size(), current_deque_size)
                    self.assertEqual(self.deque.peekFront(), head_value)
                    self.assertEqual(self.deque.peekTail(), tail_value)
                    continue
                if current_deque_size == 0 and perform_add and perform_on_tail:
                    head_value = tail_value = value
                    current_deque_size += 1
                    self.deque.addTail(value)
                    self.assertEqual(self.deque.size(), current_deque_size)
                    self.assertEqual(self.deque.peekFront(), head_value)
                    self.assertEqual(self.deque.peekTail(), tail_value)
                    continue
unittest.main()
