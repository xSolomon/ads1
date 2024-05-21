''' Tests for lesson 7 tasks 1-6 solution. '''

import unittest
from random import randint
from parametrize import parametrize
from solution7_1 import Node, OrderedList, OrderedStringList

class OrderedListTests(unittest.TestCase):
    ''' Tests for compare, add, find, delete, clean and len function. '''
    def setUp(self) -> None:
        ''' Test preparation. '''
        self.list : OrderedList = OrderedList(True)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        del self.list

    def test_compare_on_ints_and_empty_list(self) -> None:
        ''' List head, tail and len unchanged. Expect:
            1 if v1 > v2.
            0 if v1 == v2.
            -1 if v1 < v2. '''
        compare_list : list[int] = [-1, 0, 1]
        for v2 in compare_list:
            with self.subTest(v1 = 0, v2 = v2):
                self.assertEqual(self.list.compare(0, v2), -v2)
                self.assertIsNone(self.list.head)
                self.assertIsNone(self.list.tail)
                self.assertEqual(self.list.len(), 0)

    def test_len_on_empty_list(self) -> None:
        ''' Tests len on empty list. Expected 0. '''
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        self.assertEqual(self.list.len(), 0)

    def test_delete_on_empty_list(self) -> None:
        ''' Tests delete on empty list. Expected no changes to
        list head, tail and len. '''
        self.list.delete(3)
        self.list.delete(None)
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        self.assertEqual(self.list.len(), 0)

    def test_find_on_empty_list(self) -> None:
        ''' Tests find on empty list. Expected to return None,
        list head, tail and len must stay same. '''
        self.assertIsNone(self.list.find(None))
        self.assertIsNone(self.list.find(5))
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        self.assertEqual(self.list.len(), 0)

    def test_clean_on_empty_list(self) -> None:
        ''' Tests clean on empty list. Expected list head,
        tail and len unchanged. '''
        self.list.clean(True)
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        self.assertEqual(self.list.len(), 0)
        self.list.clean(False)
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        self.assertEqual(self.list.len(), 0)

    def test_add_on_ascending_empty_list(self) -> None:
        ''' Tests add on ascending empty list.
            Expected head.value = tail.value = added value.
            List len must be 1. '''
        self.list.add(5)
        self.assertIsNotNone(self.list.head)
        self.assertIsNotNone(self.list.tail)
        self.assertEqual(self.list.len(), 1)
        self.assertEqual(self.list.head.value, 5)
        self.assertEqual(self.list.tail.value, 5)

    def test_add_on_descending_empty_list(self) -> None:
        ''' Tests add on descending empty list.
            Expected head.value = tail.value = added value.
            List len must be 1. '''
        self.list.clean(False)
        self.list.add(5)
        self.assertIsNotNone(self.list.head)
        self.assertIsNotNone(self.list.tail)
        self.assertEqual(self.list.len(), 1)
        self.assertEqual(self.list.head.value, 5)
        self.assertEqual(self.list.tail.value, 5)

    def test_clean_on_singleval_list(self) -> None:
        ''' Expected list len = 0, head = tail = None. '''
        self.list.add(5)
        self.list.clean(True)
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        self.assertEqual(self.list.len(), 0)

    def test_find_non_existing_val_on_singleval_list(self) -> None:
        ''' Tests asc and desc lists. Expected "None" return result.
            List len, head and tail unchanged. '''
        for _ in range(2):
            self.list.add(5)
            with self.subTest():
                self.assertIsNone(self.list.find(6))
                self.assertIsNotNone(self.list.head)
                self.assertIsNotNone(self.list.tail)
                self.assertEqual(self.list.len(), 1)
                self.assertEqual(self.list.head.value, 5)
                self.assertEqual(self.list.tail.value, 5)
            self.list.clean(False)

    def test_find_existing_val_on_singleval_list(self) -> None:
        ''' Tests asc and desc lists. Expected added val return result.
            List len, head and tail unchanged. '''
        for _ in range(2):
            self.list.add(5)
            with self.subTest():
                self.assertIs(self.list.find(5), self.list.head)
                self.assertEqual(self.list.len(), 1)
                self.assertEqual(self.list.head.value, 5)
                self.assertEqual(self.list.tail.value, 5)
            self.list.clean(False)

    def test_delete_non_existing_val_on_singleval_list(self) -> None:
        ''' Tests asc and desc lists. Expected head, tail and len unchanged. '''
        for _ in range(2):
            self.list.add(5)
            with self.subTest():
                self.list.delete(6)
                self.assertEqual(self.list.len(), 1)
                self.assertEqual(self.list.head.value, 5)
                self.assertEqual(self.list.tail.value, 5)
            self.list.clean(False)

    def test_delete_existing_val_on_singleval_list(self) -> None:
        ''' Tests asc and desc lists. Expected empty list. '''
        for _ in range(2):
            self.list.add(5)
            with self.subTest():
                self.list.delete(5)
                self.assertEqual(self.list.len(), 0)
                self.assertIsNone(self.list.head)
                self.assertIsNone(self.list.tail)
            self.list.clean(False)

    def test_add_on_asc_singleval_list(self) -> None:
        ''' Tests adding lesser, equal and greater value to ascending list.
            Expected len = 2, new Node to take its place in head (lesser/equal case)
            or in tail (greater case). '''
        val_list : list[int] = [-5, 1, 5]
        for i, val in enumerate(val_list):
            self.list.clean(True)
            self.list.add(1)
            head : Node = self.list.head
            tail : Node = self.list.tail
            with self.subTest(val = val, head = head, tail = tail):
                self.list.add(val)
                self.assertEqual(self.list.len(), 2)
                if i < 2:
                    self.assertIsNot(self.list.head, head)
                    self.assertIs(self.list.tail, tail)
                    self.assertEqual(self.list.head.value, val)
                    continue
                self.assertIs(self.list.head, head)
                self.assertIsNot(self.list.tail, tail)
                self.assertEqual(self.list.tail.value, val)

    def test_add_on_desc_singleval_list(self) -> None:
        ''' Tests adding lesser, equal and greater value to descending list.
            Expected len = 2, new Node to take its place in head (greater/equal case)
            or in tail (lesser case). '''
        val_list : list[int] = [5, 1, -5]
        for i, val in enumerate(val_list):
            self.list.clean(False)
            self.list.add(1)
            head : Node = self.list.head
            tail : Node = self.list.tail
            with self.subTest(val = val, head = head, tail = tail):
                self.list.add(val)
                self.assertEqual(self.list.len(), 2)
                if i < 2:
                    self.assertIsNot(self.list.head, head)
                    self.assertIs(self.list.tail, tail)
                    self.assertEqual(self.list.head.value, val)
                    continue
                self.assertIs(self.list.head, head)
                self.assertIsNot(self.list.tail, tail)
                self.assertEqual(self.list.tail.value, val)

    def test_add_by_creating_ascending_list_from_predefined_unsorted_val_list(self) -> None:
        ''' Expected every value of node in position i to be the same
            as in position i in sorted_val_list. '''
        predefined_val_lists : list[list[int]] = [[5, 0, -5], [5, 5, 0],
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [0, 0, 0, -1, 0, 0, 0], [1, 2, 3],
            [2, 1, 3], [3, 2, 1], [1, 3, 2], [2, 3, 1], [3, 1, 2] ]
        for val_list in predefined_val_lists:
            for val in val_list:
                self.list.add(val)
            sorted_val_list : list[int] = sorted(val_list)
            with self.subTest(unsorted_vals = val_list, sorted_vals = sorted_val_list):
                self.assertEqual(self.list.len(), len(sorted_val_list))
                current : Node = self.list.head
                for val in sorted_val_list:
                    self.assertEqual(current.value, val)
                    current = current.next
            self.list.clean(True)

    @parametrize('repeat_times', range(1))
    def test_add_by_creating_large_random_ascending_list(self, repeat_times) -> None:
        ''' Expected every element to correctly take its place. '''
        add_times : int = 100
        val_list : list[int] = [randint(-100, 100) for _ in range(add_times)]
        for val in val_list:
            self.list.add(val)
        self.assertEqual(self.list.len(), add_times)
        sorted_list : list[int] = sorted(val_list)
        current : Node = self.list.head
        for i, val in enumerate(sorted_list):
            with self.subTest(val_pos = i, val = val):
                self.assertEqual(current.value, val)
            current = current.next
        self.assertIsNone(current)

    @parametrize('repeat_times', range(1))
    def test_add_by_creating_large_random_descending_list(self, repeat_times) -> None:
        ''' Expected every element to correctly take its place. '''
        self.list.clean(False)
        add_times : int = 100
        val_list : list[int] = [randint(-100, 100) for _ in range(add_times)]
        for val in val_list:
            self.list.add(val)
        self.assertEqual(self.list.len(), add_times)
        sorted_list : list[int] = sorted(val_list, reverse = True)
        current : Node = self.list.head
        for i, val in enumerate(sorted_list):
            with self.subTest(val_pos = i, val = val):
                self.assertEqual(current.value, val)
            current = current.next
        self.assertIsNone(current)

    @parametrize('repeat_times', range(1))
    def test_delete_by_deleting_predefined_ascending_list_in_random_order(self,
        repeat_times : int) -> None:
        ''' After each deletetion, each value must have correct position. '''
        predefined_val_lists : list[list[int]] = [[5, 0, -5], [5, 5, 0],
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [0, 0, 0, -1, 0, 0, 0], [1, 2, 3],
            [2, 1, 3], [3, 2, 1], [1, 3, 2], [2, 3, 1], [3, 1, 2] ]
        for val_list in predefined_val_lists:
            for val in val_list:
                self.list.add(val)
            sorted_val_list : list[int] = sorted(val_list)
            list_len : int = len(sorted_val_list)
            current : Node = None
            for _ in range(list_len):
                delete_position : int = randint(0, len(sorted_val_list) - 1)
                with self.subTest(vals = sorted_val_list, del_pos = delete_position):
                    self.list.delete(sorted_val_list[delete_position])
                    sorted_val_list.remove(sorted_val_list[delete_position])
                    self.assertEqual(self.list.len(), len(sorted_val_list))
                    current = self.list.head
                    for val in sorted_val_list:
                        self.assertEqual(current.value, val)
                        current = current.next
            self.list.clean(True)

    @parametrize('repeat_times', range(1))
    def test_delete_on_large_random_ascending_list(self, repeat_times) -> None:
        ''' After each operation, size must shrink by 1. 
            List must retain ascending order, and deleted val must be first occurence. '''
        initial_size : int = 100
        val_list : list[int] = [randint(-100, 100) for _ in range(initial_size)]
        for val in val_list:
            self.list.add(val)
        self.assertEqual(self.list.len(), initial_size)
        sorted_list : list[int] = sorted(val_list)
        for i in range(initial_size):
            delete_position : int = randint(0, initial_size - i - 1)
            self.list.delete(sorted_list[delete_position])
            sorted_list.remove(sorted_list[delete_position])
            self.assertEqual(self.list.len(), len(sorted_list))
            current : Node = self.list.head
            for j, val in enumerate(sorted_list):
                with self.subTest(val_pos = j, val = val):
                    self.assertEqual(current.value, val)
                current = current.next

    @parametrize('repeat_times', range(1))
    def test_delete_on_large_random_descending_list(self, repeat_times) -> None:
        ''' After each operation, size must shrink by 1. 
            List must retain ascending order, and deleted val must be first occurence. '''
        self.list.clean(False)
        initial_size : int = 100
        val_list : list[int] = [randint(-100, 100) for _ in range(initial_size)]
        for val in val_list:
            self.list.add(val)
        self.assertEqual(self.list.len(), initial_size)
        sorted_list : list[int] = sorted(val_list, reverse = True)
        for i in range(initial_size):
            delete_position : int = randint(0, initial_size - i - 1)
            self.list.delete(sorted_list[delete_position])
            sorted_list.remove(sorted_list[delete_position])
            self.assertEqual(self.list.len(), len(sorted_list))
            current : Node = self.list.head
            for j, val in enumerate(sorted_list):
                with self.subTest(val_pos = j, val = val):
                    self.assertEqual(current.value, val)
                current = current.next

    @parametrize('repeat_times', range(10))
    def test_find_on_large_random_ascending_list(self, repeat_times) -> None:
        ''' Expected to find exactly first occurence of element in the list (or "None"). '''
        list_size : int = 1000
        find_times : int = 100
        for _ in range(list_size):
            self.list.add(randint(-100, 100))
        nodes_list : list[Node] = self.list.get_all()
        for _ in range(find_times):
            find_value : int = randint(-110, 110)
            with self.subTest(value = find_value):
                found : Node = nodes_list[0]
                while found is not None:
                    if found.value == find_value:
                        break
                    found = found.next
                if found is not None:
                    self.assertIs(self.list.find(find_value), found)
                    continue
                self.assertIsNone(self.list.find(find_value))

    @parametrize('repeat_times', range(10))
    def test_find_on_large_random_descending_list(self, repeat_times) -> None:
        ''' Expected to find exactly first occurence of element in the list (or "None"). '''
        self.list.clean(False)
        list_size : int = 1000
        find_times : int = 1000
        for _ in range(list_size):
            self.list.add(randint(-100, 100))
        nodes_list : list[Node] = self.list.get_all()
        for _ in range(find_times):
            find_value : int = randint(-110, 110)
            with self.subTest(value = find_value):
                found : Node = nodes_list[0]
                while found is not None:
                    if found.value == find_value:
                        break
                    found = found.next
                if found is not None:
                    self.assertIs(self.list.find(find_value), found)
                    continue
                self.assertIsNone(self.list.find(find_value))

class OrderedStringListTests(unittest.TestCase):
    ''' Tests for compare function. '''
    def setUp(self) -> None:
        ''' Test preparation. '''
        self.list : OrderedList = OrderedStringList(True)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        del self.list

    def test_compare_on_some_predefined_strings(self) -> None:
        ''' Expected same result as in predefined list. '''
        predefined_strings_list : list[tuple(str, str)] = [('', ''), ('', '1'),
            ('1', ''), ('abak', 'aba'), ('abak', 'abak'), ('aba', 'abak')]
        result_list : list[int] = [0, -1, 1, 1, 0, -1]
        for i, result in enumerate(result_list):
            with self.subTest(strings_to_compare = predefined_strings_list[i],
                expected_result = result):
                self.assertEqual(self.list.compare(predefined_strings_list[i][0],
                    predefined_strings_list[i][1]), result)

unittest.main()
