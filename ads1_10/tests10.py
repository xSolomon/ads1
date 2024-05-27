''' Tests for lesson 10 solution. '''

import unittest
import timeit
from random import randint
from solution10 import PowerSet

class PowerSetTests(unittest.TestCase):
    ''' Tests for size, put, get, remove, intersection, union, difference, issubset methods. '''
    def setUp(self) -> None:
        ''' Test preparation. '''
        self.set : PowerSet = PowerSet()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        del self.set

    def test_size_on_empty_set(self) -> None:
        ''' Expected size = 0. '''
        self.assertEqual(self.set.size(), 0)

    def test_get_on_empty_set(self) -> None:
        ''' Expected False '''
        self.assertFalse(self.set.get(''))

    def test_issubset_on_empty_set(self) -> None:
        ''' Expected True for both sets. '''
        set2 : PowerSet = PowerSet()
        self.assertTrue(self.set.issubset(set2))
        self.assertTrue(set2.issubset(self.set))

    def test_remove_on_empty_set(self) -> None:
        ''' Expected False '''
        self.assertFalse(self.set.remove(''))

    def test_put_on_empty_set(self) -> None:
        ''' Expected size = 1 and get() to return True. '''
        self.set.put('')
        self.assertEqual(self.set.size(), 1)
        self.assertTrue(self.set.get(''))

    def test_union_on_two_empty_sets(self) -> None:
        ''' Expected size = 0. '''
        set2 : PowerSet = PowerSet()
        result_set : PowerSet = self.set.union(set2)
        self.assertEqual(result_set.size(), 0)

    def test_difference_on_two_empty_sets(self) -> None:
        ''' Expected size = 0. '''
        set2 : PowerSet = PowerSet()
        result_set : PowerSet = self.set.difference(set2)
        self.assertEqual(result_set.size(), 0)
        result_set : PowerSet = set2.difference(self.set)
        self.assertEqual(result_set.size(), 0)

    def test_intersection_on_two_empty_sets(self) -> None:
        ''' Expected size = 0. '''
        set2 : PowerSet = PowerSet()
        result_set : PowerSet = self.set.intersection(set2)
        self.assertEqual(result_set.size(), 0)

    def test_remove_non_existing_elem_on_single_elem_set(self) -> None:
        ''' Expected unchanged set state. '''
        self.set.put('')
        self.set.remove('1')
        self.assertEqual(self.set.size(), 1)
        self.assertTrue(self.set.get(''))

    def test_remove_existing_elem_on_single_elem_set(self) -> None:
        ''' Expected size = 0 and False for get(). '''
        self.set.put('')
        self.set.remove('')
        self.assertEqual(self.set.size(), 0)
        self.assertFalse(self.set.get(''))

    def test_issubset_on_two_equal_single_elem_sets(self) -> None:
        ''' Expected True for both sets. '''
        set2 : PowerSet = PowerSet()
        self.set.put('')
        set2.put('')
        self.assertTrue(self.set.issubset(set2))
        self.assertTrue(set2.issubset(self.set))

    def test_intersection_on_two_equal_single_elem_sets(self) -> None:
        ''' Expected equal set. '''
        set2 : PowerSet = PowerSet()
        self.set.put('')
        set2.put('')
        result : PowerSet = self.set.intersection(set2)
        self.assertEqual(result.size(), 1)
        self.assertTrue(result.get(''))

    def test_difference_on_two_equal_single_elem_sets(self) -> None:
        ''' Expected empty set for both sets. '''
        set2 : PowerSet = PowerSet()
        self.set.put('')
        set2.put('')
        result : PowerSet = self.set.difference(set2)
        self.assertEqual(result.size(), 0)
        result : PowerSet = set2.difference(self.set)
        self.assertEqual(result.size(), 0)

    def test_union_on_two_equal_single_elem_sets(self) -> None:
        ''' Expected equal set. '''
        set2 : PowerSet = PowerSet()
        self.set.put('')
        set2.put('')
        result : PowerSet = self.set.union(set2)
        self.assertEqual(result.size(), 1)
        self.assertTrue(result.get(''))

    def test_put_same_elem_in_sigle_elem_set(self) -> None:
        ''' Expected set state unchanged. '''
        self.set.put('')
        self.set.put('')
        self.assertEqual(self.set.size(), 1)
        self.assertTrue(self.set.get(''))

    def test_put_in_single_elem_set(self) -> None:
        ''' Expected size = 2 and get() to return True. '''
        self.set.put('1')
        self.set.put('2')

        self.assertEqual(self.set.size(), 2)
        self.assertTrue(self.set.get('2'))

    def test_issubset_on_two_unequal_single_elem_sets(self) -> None:
        ''' Expected False for both cases. '''
        set2 : PowerSet = PowerSet()
        set2.put('1')
        self.set.put('2')
        self.assertFalse(self.set.issubset(set2))
        self.assertFalse(set2.issubset(self.set))

    def test_difference_on_two_unequal_single_elem_sets(self) -> None:
        ''' Expected diminishing set for both cases. '''
        set2 : PowerSet = PowerSet()
        set2.put('1')
        self.set.put('2')
        result : PowerSet = self.set.difference(set2)
        self.assertEqual(result.size(), 1)
        self.assertTrue(result.get('2'))
        result : PowerSet = set2.difference(self.set)
        self.assertEqual(result.size(), 1)
        self.assertTrue(result.get('1'))

    def test_intersection_on_two_unequal_single_elem_set(self) -> None:
        ''' Expected empty set for both cases. '''
        self.set.put('')
        set2 : PowerSet = PowerSet()
        set2.put('1')
        result : PowerSet = self.set.intersection(set2)
        self.assertEqual(result.size(), 0)
        result : PowerSet = set2.intersection(self.set)
        self.assertEqual(result.size(), 0)

    def test_union_on_two_unequal_single_elem_sets(self) -> None:
        ''' Expected size = 2 and True for key from both sets. '''
        self.set.put('1')
        set2 : PowerSet = PowerSet()
        set2.put('2')
        result : PowerSet = self.set.union(set2)
        self.assertEqual(result.size(), 2)
        self.assertTrue(result.get('1'))
        self.assertTrue(result.get('2'))
        result : PowerSet = set2.union(self.set)
        self.assertEqual(result.size(), 2)
        self.assertTrue(result.get('1'))
        self.assertTrue(result.get('2'))

    def test_union_on_some_predefined_sets(self) -> None:
        ''' Expected result set to be same as corresponding set in result list. '''
        tested_set_list : list[str] = ['1', '2', '3']
        for elem in tested_set_list:
            self.set.put(elem)
        set_lists : list[list[str]] = [[''], ['1'], ['1', '2'], ['1', '2', '3', '4', '5'],
            ['1', '2', '3', '4', '5', '6'], ['7', '8', '9', '10', '11']]
        result_set_lists : list[list[str]] = [['', '1', '2', '3'], ['1', '2', '3'], ['1', '2', '3'],
            ['1', '2', '3', '4', '5'], ['1', '2', '3', '4', '5', '6'],
            ['1', '2', '3', '7', '8', '9', '10', '11']]
        for i, set_list in enumerate(set_lists):
            set2 : PowerSet = PowerSet()
            for elem in set_list:
                set2.put(elem)
            with self.subTest(first_set = tested_set_list, second_set = set_list):
                result_set : PowerSet = self.set.union(set2)
                self.assertEqual(result_set.size(), len(result_set_lists[i]))
                for elem in result_set_lists[i]:
                    self.assertTrue(result_set.get(elem))

    def test_intersection_on_some_predefined_sets(self) -> None:
        ''' Expected result set to be same as corresponding set in result list. '''
        tested_set_list : list[str] = ['1', '2', '3']
        for elem in tested_set_list:
            self.set.put(elem)
        set_lists : list[list[str]] = [[''], ['1'], ['1', '2'], ['1', '2', '3', '4', '5'],
            ['1', '2', '3', '4', '5', '6'], ['7', '8', '9', '10', '11']]
        result_set_lists : list[list[str]] = [[], ['1'], ['1', '2'],
            ['1', '2', '3'], ['1', '2', '3'],
            []]
        for i, set_list in enumerate(set_lists):
            set2 : PowerSet = PowerSet()
            for elem in set_list:
                set2.put(elem)
            with self.subTest(first_set = tested_set_list, second_set = set_list):
                result_set : PowerSet = self.set.intersection(set2)
                self.assertEqual(result_set.size(), len(result_set_lists[i]))
                for elem in result_set_lists[i]:
                    self.assertTrue(result_set.get(elem))

    def test_difference_on_some_predefined_sets(self) -> None:
        ''' Expected result set to be same as corresponding set in result list. '''
        tested_set_list : list[str] = ['1', '2', '3']
        for elem in tested_set_list:
            self.set.put(elem)
        set_lists : list[list[str]] = [[''], ['1'], ['1', '2'], ['1', '2', '3', '4', '5'],
            ['1', '2', '3', '4', '5', '6'], ['7', '8', '9', '10', '11']]
        result_set_lists : list[list[str]] = [['1', '2', '3'], ['2', '3'], ['3'],
            [], [], ['1', '2', '3']]
        for i, set_list in enumerate(set_lists):
            set2 : PowerSet = PowerSet()
            for elem in set_list:
                set2.put(elem)
            with self.subTest(first_set = tested_set_list, second_set = set_list):
                result_set : PowerSet = self.set.difference(set2)
                self.assertEqual(result_set.size(), len(result_set_lists[i]))
                for elem in result_set_lists[i]:
                    self.assertTrue(result_set.get(elem))

    def test_issubset_on_some_predefined_sets(self) -> None:
        ''' Expected result set to be same as corresponding set in result list. '''
        tested_set_list : list[str] = ['1', '2', '3']
        for elem in tested_set_list:
            self.set.put(elem)
        set_lists : list[list[str]] = [[''], ['1'], ['1', '2'], ['1', '2', '3', '4', '5'],
            ['1', '2', '3', '4', '5', '6'], ['7', '8', '9', '10', '11']]
        result_set_lists : list[tuple[bool]] = [(False, False), (True, False), (True, False),
            (False, True), (False, True), (False, False)]
        for i, set_list in enumerate(set_lists):
            set2 : PowerSet = PowerSet()
            for elem in set_list:
                set2.put(elem)
            with self.subTest(first_set = tested_set_list, second_set = set_list):
                self.assertEqual(self.set.issubset(set2), result_set_lists[i][0])
                self.assertEqual(set2.issubset(self.set), result_set_lists[i][1])

    def test_put_on_some_predefined_sets(self) -> None:
        ''' Expected result set to be same as corresponding set in result list. '''
        tested_set_list : list[str] = ['1', '2', '3']
        set_lists : list[list[str]] = [[''], ['1'], ['1', '2'], ['1', '2', '3', '4', '5'],
            ['1', '2', '3', '4', '5', '6'], ['7', '8', '9', '10', '11']]
        result_set_lists : list[list[str]] = [['', '1', '2', '3'], ['1', '2', '3'],
        ['1', '2', '3'], ['1', '2', '3', '4', '5'], ['1', '2', '3', '4', '5', '6'],
        ['1', '2', '3', '7', '8', '9', '10', '11']]
        for i, set_list in enumerate(set_lists):
            test_set : PowerSet = PowerSet()
            for elem in tested_set_list:
                test_set.put(elem)
            for elem in set_list:
                test_set.put(elem)
            with self.subTest(first_set = tested_set_list, second_set = set_list):
                self.assertEqual(test_set.size(), len(result_set_lists[i]))
                for elem in result_set_lists[i]:
                    self.assertTrue(test_set.get(elem))
            del test_set

    def test_ops_time_on_tens_of_thousands_elems(self) -> None:
        ''' Every operation must be no longer than 2-3 seconds. '''
        set_size : int = 70000
        set1 : PowerSet = PowerSet()
        set2 : PowerSet = PowerSet()
        for _ in range(set_size):
            set1.put(randint(-100000, 1000000))
            set2.put(randint(-1000000, 100000))
        result_set : PowerSet = PowerSet()
        result_set  = set1.intersection(set2)
        self.assertGreaterEqual(result_set.size(), 0)
        result_set = set1.difference(set2)
        self.assertGreaterEqual(result_set.size(), 0)
        result_set = set1.union(set2)
        self.assertGreaterEqual(result_set.size(), 0)
        result : bool = set1.issubset(set2)
        self.assertFalse(result)


unittest.main()
