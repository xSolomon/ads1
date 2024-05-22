''' Tests for lesson 8 solution. '''

import unittest
import string
from random import choice
from solution8_1 import HashTable

class HashTableTests(unittest.TestCase):
    ''' Tests for hash_fun, seek_slot, put, find methods. '''
    def setUp(self) -> None:
        ''' Test preparation. '''
        self.table : HashTable = HashTable(17, 3)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.table.slots = []
        del self.table

    def test_hash_fun_on_random_strings_and_empty_table(self) -> None:
        ''' Expected correct index value for each string. '''
        test_times : int = 1000
        str_len : int = 100
        test_string : str
        char_pool : str = string.ascii_letters + string.punctuation + string.digits
        for _ in range(test_times):
            test_string = ''.join(choice(char_pool) for _ in range(str_len))
            with self.subTest(string = test_string):
                slot : int = self.table.hash_fun(test_string)
                self.assertGreaterEqual(slot, 0)
                self.assertLess(slot, self.table.size)

    def test_seek_slot_on_random_strings_and_empty_table(self) -> None:
        ''' Expected slot = hash_fun from corresponding string. '''
        test_times : int = 1000
        str_len : int = 100
        test_string : str
        char_pool : str = string.ascii_letters + string.punctuation + string.digits
        for _ in range(test_times):
            test_string = ''.join(choice(char_pool) for _ in range(str_len))
            with self.subTest(string = test_string):
                slot : int = self.table.hash_fun(test_string)
                self.assertIsNotNone(slot)
                self.assertEqual(self.table.seek_slot(test_string), slot)

    def test_find_slot_on_random_strings_and_empty_table(self) -> None:
        ''' Expected slot = None for each string. '''
        test_times : int = 1000
        str_len : int = 100
        test_string : str
        char_pool : str = string.ascii_letters + string.punctuation + string.digits
        for _ in range(test_times):
            test_string = ''.join(choice(char_pool) for _ in range(str_len))
            with self.subTest(string = test_string):
                self.assertIsNone(self.table.find(test_string))

    def test_put_on_random_strings_and_empty_table(self) -> None:
        ''' Expected slot = has_fun from corresponding string. '''
        test_times : int = 1000
        str_len : int = 100
        test_string : str
        char_pool : str = string.ascii_letters + string.punctuation + string.digits
        for _ in range(test_times):
            test_string = ''.join(choice(char_pool) for _ in range(str_len))
            slot : int = self.table.hash_fun(test_string)
            with self.subTest(string = test_string, expected_slot = slot):
                self.assertEqual(self.table.put(test_string), slot)
                self.assertEqual(self.table.slots[slot], test_string)
                self.table.slots[slot] = None

    def test_seek_slot_on_full_table(self) -> None:
        ''' Expected slot = "None" for every try. '''
        test_times : int = 1000
        str_len : int = 100
        test_string : str
        table_slot_vals_list : list[str] = [None] * self.table.size
        char_pool : str = string.ascii_letters + string.punctuation + string.digits
        for _ in self.table.slots:
            test_string = ''.join(choice(char_pool) for _ in range(str_len))
            slot_pos = self.table.put(test_string)
            self.assertIsNotNone(slot_pos)
            table_slot_vals_list[slot_pos] = test_string
        for i, val, in enumerate(table_slot_vals_list):
            self.assertEqual(self.table.find(val), i)
            self.assertIsNotNone(self.table.slots[i])
            self.assertEqual(self.table.slots[i], val)
        for _ in range(test_times):
            test_string = ''.join(choice(char_pool) for _ in range(str_len))
            with self.subTest(string = test_string):
                self.assertIsNone(self.table.seek_slot(test_string))

    def test_put_on_full_table(self) -> None:
        ''' Expected slot = "None" for every try. '''
        test_times : int = 1000
        str_len : int = 100
        test_string : str
        table_slot_vals_list : list[str] = [None] * self.table.size
        char_pool : str = string.ascii_letters + string.punctuation + string.digits
        for _ in self.table.slots:
            test_string = ''.join(choice(char_pool) for _ in range(str_len))
            slot_pos = self.table.put(test_string)
            self.assertIsNotNone(slot_pos)
            table_slot_vals_list[slot_pos] = test_string
        for i, val, in enumerate(table_slot_vals_list):
            self.assertEqual(self.table.find(val), i)
            self.assertIsNotNone(self.table.slots[i])
            self.assertEqual(self.table.slots[i], val)
        for _ in range(test_times):
            test_string = ''.join(choice(char_pool) for _ in range(str_len))
            with self.subTest(string = test_string):
                self.assertIsNone(self.table.put(test_string))

unittest.main()
