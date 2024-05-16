''' Tests for solution 1.8. '''

import unittest
from random import randint
from solution_1_1 import LinkedList, Node
from solution_1_8 import merge_lists_by_adding_their_elements as merge

class MergeTests(unittest.TestCase):
    ''' Tests merge_lists_by_adding_their_elements() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.first : LinkedList = LinkedList()
        self.second : LinkedList = LinkedList()
        self.result : list[LinkedList, bool] = []

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        del self.first
        del self.second
        self.result = []

    def check(self, expected : list[LinkedList, bool]) -> None:
        ''' Checks if function result is the same as expected. '''
        self.assertEqual(expected[1], self.result[1])
        self.assertEqual(expected[0].len(), self.result[0].len())
        expected_current = expected[0].head
        result_current = self.result[0].head
        while expected_current is not None:
            self.assertEqual(expected_current.value, result_current.value)
            expected_current = expected_current.next
            result_current = result_current.next

    def test_empty_lists(self) -> None:
        ''' Test on two empty lists. '''
        self.result = merge(self.first, self.second)
        self.check([LinkedList(), True])

    def test_one_empty_list(self) -> None:
        ''' Test on one empty and one singleval list. '''
        for i in range(2):
            if i == 0:
                self.first.add_in_tail(Node(0))
            else:
                self.second.add_in_tail(Node(0))
            with self.subTest():
                self.result = merge(self.first, self.second)
                self.check([LinkedList(), False])
            self.first.clean()
            self.second.clean()

    def test_regression_same_length(self) -> None:
        ''' Tests on two lists: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and reversed.
            Expected result list: [11, 11, 11, 11, 11, 11, 11, 11, 11, 11] '''
        expected_list : LinkedList = LinkedList()
        for i in range(10):
            self.first.add_in_tail(Node(i + 1))
            self.second.add_in_tail(Node(10 - i))
            expected_list.add_in_tail(Node(11))
        self.result = merge(self.first, self.second)
        self.check([expected_list, True])
        expected_list.clean()

    def test_on_large_random_lists(self) -> None:
        ''' Test on two large lists with random values and same length. '''
        expected_list : LinkedList = LinkedList()
        for _ in range(10000):
            first_number : int = randint(-100, 100)
            second_number : int = randint(-100, 100)
            expected_list.add_in_tail(Node(first_number + second_number))
            self.first.add_in_tail(Node(first_number))
            self.second.add_in_tail(Node(second_number))
        self.result = merge(self.first, self.second)
        self.check([expected_list, True])
        expected_list.clean()


unittest.main()
