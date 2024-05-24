''' Tests for lesson 9 solution. '''

import unittest
from solution9_1 import NativeDictionary

class HashTableTests(unittest.TestCase):
    ''' Tests for put, get, is_key methods. '''
    def setUp(self) -> None:
        ''' Test preparation. '''
        self.table : NativeDictionary = NativeDictionary(17)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.table.slots = []
        self.table.values = []
        del self.table

    def test_is_key_on_empty_table(self) -> None:
        ''' Expected False. '''
        self.assertFalse(self.table.is_key(''))

    def test_get_on_empty_table(self) -> None:
        ''' Expected "None". '''
        self.assertIsNone(self.table.get(''))

    def test_put_on_empty_table(self) -> None:
        ''' Expected to put value exactly on pos from hash_function. '''
        pos : int = self.table.hash_fun('')
        self.table.put('', 1)
        self.assertEqual(self.table.slots[pos], '')
        self.assertEqual(self.table.values[pos], 1)

    def test_is_key_in_one_elem_table(self) -> None:
        ''' Expected True for putted key and False otherwise. '''
        self.table.put('', 1)
        self.assertTrue(self.table.is_key(''))
        self.assertFalse(self.table.is_key('1'))

    def test_get_on_single_elem_table(self) -> None:
        ''' Expected putted value for existing key, "None" otherwise. '''
        self.table.put('', 1)
        self.assertEqual(self.table.get(''), 1)
        self.assertIsNone(self.table.get('1'))

    def test_by_creating_full_table(self) -> None:
        ''' Expected all keys to be successfully added. 
            Also is_key and get to provide correct values.
            Finally, expect successful write by existing keys. '''
        for i in range(self.table.size):
            self.table.put(str(i), i)
        for i in range(self.table.size):
            self.assertTrue(self.table.is_key(str(i)))
            self.assertEqual(self.table.get(str(i)), i)
        for i in range(self.table.size):
            self.table.put(str(i), i ** 2)
        for i in range(self.table.size):
            self.assertTrue(self.table.is_key(str(i)))
            self.assertEqual(self.table.get(str(i)), i ** 2)

unittest.main()
