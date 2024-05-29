
''' Tests for lesson 12 solution. '''

import unittest
from random import randint
from solution12 import NativeCache

class CacheTests(unittest.TestCase):
    ''' Tests for put, get, is_key methods. '''
    def setUp(self) -> None:
        ''' Test preparation. '''
        self.cache : NativeCache = NativeCache(17)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.cache.slots = []
        self.cache.values = []
        self.cache.hits = []
        del self.cache

    def test_is_key_on_empty_cache(self) -> None:
        ''' Expected False. '''
        self.assertFalse(self.cache.is_key(''))

    def test_get_on_empty_cache(self) -> None:
        ''' Expected "None". '''
        self.assertIsNone(self.cache.get(''))

    def test_put_on_empty_cache(self) -> None:
        ''' Expected to put value exactly on pos from hash_function. '''
        pos : int = self.cache.hash_fun('')
        self.cache.put('', 1)
        self.assertEqual(self.cache.slots[pos], '')
        self.assertEqual(self.cache.values[pos], 1)
        self.assertEqual(self.cache.hits[pos], 1)

    def test_is_key_in_one_elem_cache(self) -> None:
        ''' Expected True for putted key and False otherwise. '''
        self.cache.put('', 1)
        self.assertTrue(self.cache.is_key(''))
        self.assertFalse(self.cache.is_key('1'))

    def test_get_on_single_elem_cache(self) -> None:
        ''' Expected putted value for existing key, "None" otherwise. '''
        self.cache.put('', 1)
        self.assertEqual(self.cache.get(''), 1)
        self.assertIsNone(self.cache.get('1'))

    def test_by_creating_full_cache(self) -> None:
        ''' Expected all keys to be successfully added. 
            Also is_key and get to provide correct values.
            Finally, expect successful write by existing keys. '''
        for i in range(self.cache.size):
            self.cache.put(str(i), i)
        for i in range(self.cache.size):
            self.assertTrue(self.cache.is_key(str(i)))
            self.assertEqual(self.cache.get(str(i)), i)
        for i in range(self.cache.size):
            with self.subTest():
                self.assertEqual(self.cache.hits[i], 2)
        for i in range(self.cache.size):
            self.cache.put(str(i), i ** 2)
        for i in range(self.cache.size):
            self.assertTrue(self.cache.is_key(str(i)))
            self.assertEqual(self.cache.get(str(i)), i ** 2)
        for i in range(self.cache.size):
            with self.subTest():
                self.assertEqual(self.cache.hits[i], 4)

    def test_by_replacing_key_with_least_hits(self) -> None:
        ''' Expected hits increasing after each access by corresponding key.
            Also expected key with least hits to be replaced by new key. '''
        for i in range(self.cache.size):
            self.cache.put(str(i), i)
        key_list : list[str] = [key for key in self.cache.slots]
        key_hits_list : list[int] = [hits for hits in self.cache.hits]
        total_key_access : int = 1000
        for _ in range(total_key_access):
            key : int = randint(0, self.cache.size - 1)
            key_hits_list[key] += 1
            self.cache.get(key_list[key])
        for i in range(self.cache.size):
            with self.subTest():
                self.assertEqual(key_hits_list[i], self.cache.hits[i])
        replace_times : int = 10
        for i in range(replace_times):
            expected_pos : int = self.cache.hits.index(min(self.cache.hits))
            with self.subTest(i = i, expected_pos = expected_pos):
                self.cache.put(str(1000 + 2 ** i), 1000 + 2 ** i)
                self.assertEqual(self.cache.hits[expected_pos], 1)
            for _ in range(1000):
                self.cache.get(str(1000 + 2 ** i))


unittest.main()
