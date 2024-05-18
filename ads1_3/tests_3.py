''' Tests for DynArray insert and delete functions. '''
import unittest
from random import randint
from solution_3 import DynArray

class DynArrayInsertTests(unittest.TestCase):
    ''' Tests DynArray insert() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.ary = DynArray()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        for i in range(len(self.ary), 0, -1):
            self.ary.delete(i - 1)
        del self.ary

    def test_insert_by_invalid_index_in_empty_ary(self) -> None:
        ''' Tests insertion in empty ary by index that don't exist. '''
        self.assertRaises(IndexError, self.ary.insert, -1, 0)
        self.assertRaises(IndexError, self.ary.insert, len(self.ary) + 1, 0)

    def test_insert_by_invalid_index_in_single_elem_ary(self) -> None:
        ''' Tests insertion in single item ary by index that don't exist. '''
        self.ary.append(5)
        self.assertRaises(IndexError, self.ary.insert, -1, 0)
        self.assertRaises(IndexError, self.ary.insert, len(self.ary) + 1, 0)

    def test_insert_by_invalid_index_in_large_random_ary(self) -> None:
        ''' Tests insertion in large ary with random vals by index that don't exist. '''
        starting_len : int = 100
        final_len : int = 1500
        for _ in range(starting_len):
            self.ary.append(randint(1, 100))
        for _ in range(starting_len, final_len):
            self.ary.append(randint(1, 100))
            with self.subTest():
                self.assertRaises(IndexError, self.ary.insert, -1, 0)
                self.assertRaises(IndexError, self.ary.insert, len(self.ary) + 1, 0)

    def test_insert_in_empty_list(self) -> None:
        ''' Tests insertion in empty ary. '''
        self.ary.insert(0, 2)
        self.assertEqual(self.ary[0], 2)
        self.assertEqual(len(self.ary), 1)
        self.assertEqual(self.ary.capacity, 16)

    def test_insert_in_single_elem_ary(self) -> None:
        ''' Tests insertion in ary with single elem. 
            Tests insertion before and after cases.'''
        self.ary.append(2)
        for i in range(2):
            with self.subTest():
                self.ary.insert(i, 5)
                self.assertEqual(self.ary[i], 5)
                self.assertEqual(len(self.ary), 2)
                self.assertEqual(self.ary.capacity, 16)
            self.ary.delete(i)

    def test_inser_in_ary_with_free_buffer_space(self) -> None:
        ''' Tests insertion in ary with elem count < capacity.
            Buffer must'nt increase. '''
        for _ in range(self.ary.capacity):
            with self.subTest():
                self.ary.insert(0, randint(0, 100))
                self.assertEqual(self.ary.capacity, 16)

    def test_insert_in_ary_with_full_buffer(self) -> None:
        ''' Tests insertion in ary with elem count == buffer size.
            Element must be inserted and buffer size must increase. '''
        buffer_increase_times : int = 15
        for _ in range(9):
            self.ary.append(randint(1, 100))
        for i in range(4, buffer_increase_times + 4):
            for _ in range(2 ** (i - 1) - 1):
                self.ary.append(randint(1, 100))
            with self.subTest():
                self.ary.insert(len(self.ary), 2 ** i)
                self.assertEqual(self.ary[2 ** i], 2 ** i)
                self.assertEqual(len(self.ary), 2 ** i + 1)
                self.assertEqual(self.ary.capacity, 2 ** (i + 1))

    def test_insert_large_random(self) -> None:
        ''' Tests insertion in random positions (even impossible).
            Checks buffer capacity correctness, inserted value and
            IndexException if index is incorrect. '''
        insertion_tries : int = 1000
        capacity : int = 16
        for _ in range(insertion_tries):
            insertion_index : int = randint(-2, len(self.ary) + 2)
            with self.subTest(ary_len = len(self.ary), index = insertion_index):
                if insertion_index < 0 or insertion_index > len(self.ary):
                    self.assertRaises(IndexError, self.ary.insert, insertion_index, randint(1, 100))
                    self.assertEqual(self.ary.capacity, capacity)
                    return
                if self.ary.count == capacity:
                    capacity *= 2
                val : int = randint(1, 100)
                self.ary.insert(insertion_index, val)
                self.assertEqual(self.ary.capacity, capacity)
                self.assertEqual(self.ary[insertion_index], val)

class DynArrayDeleteTests(unittest.TestCase):
    ''' Tests DynArray delete() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.ary = DynArray()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        for i in range(len(self.ary), 0, -1):
            self.ary.delete(i - 1)
        del self.ary

    def test_delete_by_invalid_index_in_empty_ary(self) -> None:
        ''' Tests deletion in empty ary by index that don't exist. '''
        self.assertRaises(IndexError, self.ary.delete, -1)
        self.assertRaises(IndexError, self.ary.delete, len(self.ary))
        self.assertRaises(IndexError, self.ary.delete, len(self.ary) + 1)

    def test_delete_by_invalid_index_in_single_elem_ary(self) -> None:
        ''' Tests deletion in single item ary by index that don't exist. '''
        self.ary.append(5)
        self.assertRaises(IndexError, self.ary.delete, -1)
        self.assertRaises(IndexError, self.ary.delete, len(self.ary) + 1)

    def test_delete_in_two_elem_ary(self) -> None:
        ''' Tests cases whe deleting first and last element. If first is deleted,
            second elem must shift to its place. '''
        self.ary.append(5)
        for i in range(2):
            self.ary.append(10)
            with self.subTest():
                self.ary.delete(i)
                if i == 0:
                    self.assertEqual(self.ary[i], 10)
                else:
                    self.assertEqual(self.ary[i - 1], 10)
                self.assertEqual(len(self.ary), 1)
                self.assertEqual(self.ary.capacity, 16)

    def test_full_deletion_of_ary_with_min_buffer(self) -> None:
        ''' Tests full deletion of capacity = count = 16 ary. No shrink is allowed.
            Remaining items must shift left. '''
        for i in range(self.ary.capacity):
            self.ary.append(i)
        for i in range(self.ary.capacity):
            self.ary.delete(0)
            with self.subTest(i = i, len = self.ary.count):
                for j in range(self.ary.count):
                    self.assertEqual(self.ary[j], j + i + 1)
                self.assertEqual(len(self.ary), self.ary.capacity - 1 - i)
                self.assertEqual(self.ary.capacity, 16)

    def test_full_deletion_of_ary_with_large_buffer(self) -> None:
        ''' Tests full deletion of large array. After certain deletions,
            buffer must shrink by 1.5 times. '''
        initial_size : int = 300
        for _ in range(10):
            for i in range(initial_size):
                self.ary.append(i)
            capacity : int = self.ary.capacity
            next_shrink_count : int = int(self.ary.capacity / 1.5)
            if next_shrink_count < 16:
                next_shrink_count = 0
            for i in range(initial_size):
                self.ary.delete(0)
                if len(self.ary) * 2 < capacity:
                    capacity = max(next_shrink_count, 16)
                    next_shrink_count = int(self.ary.capacity / 1.5)
                if next_shrink_count < 16:
                    next_shrink_count = 0
                with self.subTest(i = i, len = self.ary.count):
                    for j in range(self.ary.count):
                        self.assertEqual(self.ary[j], j + i + 1)
                    self.assertEqual(self.ary.capacity, capacity)

unittest.main()
