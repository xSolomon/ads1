''' Tests for lesson 11 solution. '''

import unittest
import string
from random import choice
from collections import deque
from solution11 import BloomFilter

class BloomFilterTests(unittest.TestCase):
    ''' Tests for hash1, hash2, add, is_value functions. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.filter : BloomFilter = BloomFilter(32)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        del self.filter

    def test_hashes_on_empty_filter(self) -> None:
        ''' Expected 0 <= pos <= 31 for each function. '''
        tries : int = 10000
        str_len : int = 100
        char_pool : str = string.ascii_letters + string.punctuation + string.digits
        for _ in range(tries):
            test_string = ''.join(choice(char_pool) for _ in range(str_len))
            with self.subTest():
                pos1 : int = self.filter.hash1(test_string)
                pos2 : int = self.filter.hash2(test_string)
                self.assertGreaterEqual(pos1, 0)
                self.assertGreaterEqual(pos2, 0)
                self.assertLess(pos1, self.filter.filter_len)
                self.assertLess(pos2, self.filter.filter_len)

    def test_is_value_on_empty_filter(self) -> None:
        ''' Expected False for each key. '''
        key_list : list[str] = ['', '1', 'qwerty', ' ', '', '']
        for key in key_list:
            with self.subTest():
                self.assertFalse(self.filter.is_value(key))

    def test_add_on_empty_filter(self) -> None:
        ''' Expected is_value to return True. '''
        key : str = "1"
        self.filter.add(key)
        self.assertTrue(self.filter.is_value(key))

    def test_filter_on_predefined_strings(self) -> None:
        ''' Expected each is_value = True for each string. '''
        test_string : deque = deque("9012345678")
        string_list : list[str] = []
        for _ in range(10):
            test_string.rotate(-1)
            string_list.append(''.join(test_string))
        for i, s in enumerate(string_list):
            with self.subTest(i = i, string = s):
                self.filter.add(s)
                for _ in range(i + 1):
                    self.assertTrue(self.filter.is_value(string_list[i]))

unittest.main()
