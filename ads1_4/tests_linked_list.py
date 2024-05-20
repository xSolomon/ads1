''' Tests for LinkedList. '''

import unittest
from random import randint, sample
from functools import reduce
from parametrize import parametrize
from linked_list import Node, LinkedList, LinkedListIterator

class LinkedListDeleteFirstOccuredValTests(unittest.TestCase):
    ''' Tests for LinkedList delete() function, with flag all=false. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList = LinkedList()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        del self.test_list

    def test_empty_list(self) -> None:
        ''' Tests empty list. '''
        self.test_list.delete(13)
        self.assertIsNone(self.test_list.get_head())
        self.assertIsNone(self.test_list.get_tail())

    @parametrize('node_val, val_to_delete', [(128, 64), (128, 127), (0, 1), (-1, 0)])
    def test_one_elem_list_by_deleting_non_existing_val(self, node_val : int,
        val_to_delete : int) -> None:
        ''' Tests list with single node. Tries to delete value that is not present in the list.
            Nothing must be deleted. '''
        self.test_list.insert(Node(node_val))
        self.test_list.delete(val_to_delete)
        self.assertIsNotNone(self.test_list.get_head())
        self.assertIsNotNone(self.test_list.get_tail())
        self.assertEqual(len(self.test_list), 1)
        self.assertEqual(self.test_list.get_head().value, node_val)

    @parametrize('val', [128, 0, -1, 64])
    def test_one_elem_list_by_deleting_existing_val(self, val : int) -> None:
        ''' Tests list with single node. Tries to delete value that is present in the list. 
            Resulting list must be empty. '''
        self.test_list.insert(Node(val))
        self.test_list.delete(val)
        self.assertEqual(len(self.test_list), 0)
        self.assertIsNone(self.test_list.get_head())
        self.assertIsNone(self.test_list.get_tail())

    @parametrize('repeat_times', range(100))
    def test_large_random_list_by_deleting_existing_val(self, repeat_times : int) -> None:
        ''' Tests deleting non-existent value from a large list of random values. '''
        list_len : int = 1000
        val : int = 0
        # Position where to_be_deleted value will be inserted:
        # Head.
        # Right after the head node.
        # Random place between second and tail nodes.
        # Tail.
        val_position_list : list[int] = [0, 1, randint(2, list_len - 2), list_len - 1]
        insert_pos_list : list[int] = sample(val_position_list, randint(0, len(val_position_list)))

        # Fill list with random values from 1 to 100, except positions
        # that are in the insert_position_list.
        for i in range(list_len):
            self.test_list.insert(Node(val if i in insert_pos_list else randint(1, 100)),
            None, True)
        self.test_list.delete(val)
        self.assertIsNotNone(self.test_list.get_head())
        self.assertIsNotNone(self.test_list.get_tail())
        self.assertEqual(len(self.test_list), (list_len if not insert_pos_list else list_len - 1))

        val_list : list[Node] = self.test_list.find_all(val)
        if len(insert_pos_list) <= 1:
            self.assertEqual(val_list, [])
        else:
            self.assertEqual(len(val_list), len(insert_pos_list) - 1)
            self.assertTrue(reduce(lambda x, y : x and (y.value == val), val_list, True))

class LinkedListDeleteAllOccuredValTests(unittest.TestCase):
    ''' Tests for LinkedList delete() function, with flag all=false. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList = LinkedList()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        del self.test_list

    def test_empty_list(self) -> None:
        ''' Tests empty list. '''
        self.test_list.delete(13, True)
        self.assertIsNone(self.test_list.get_head())
        self.assertIsNone(self.test_list.get_tail())
        self.assertEqual(len(self.test_list), 0)

    @parametrize('node_val, val_to_delete', [(128, 64), (128, 127), (0, 1), (-1, 0)])
    def test_one_elem_list_by_deleting_non_existing_val(self, node_val : int,
        val_to_delete : int) -> None:
        ''' Tests list with single node. Tries to delete value that is not present in the list.
            Nothing must be deleted. '''
        self.test_list.insert(Node(node_val))
        self.test_list.delete(val_to_delete, True)
        self.assertIsNotNone(self.test_list.get_head())
        self.assertIsNotNone(self.test_list.get_tail())
        self.assertEqual(len(self.test_list), 1)
        self.assertEqual(self.test_list.get_head().value, node_val)

    @parametrize('val', [128, 0, -1, 64])
    def test_one_elem_list_by_deleting_existing_val(self, val : int) -> None:
        ''' Tests list with single node. Tries to delete value that is present in the list. 
            Resulting list must be empty. '''
        self.test_list.insert(Node(val))
        self.test_list.delete(val, True)
        self.assertEqual(len(self.test_list), 0)
        self.assertIsNone(self.test_list.get_head())
        self.assertIsNone(self.test_list.get_tail())

    def test_large_list_by_deleting_non_existing_vals(self) -> None:
        ''' Tests deleting non-existent value from a large list of random values. '''
        val_list : list[int] = [-1, 101, 102, 103, 0]
        test_list_len : int = 1000
        for _ in range(test_list_len):
            self.test_list.insert(Node(randint(1, 100)), None, True)
        for val in val_list:
            with self.subTest():
                self.test_list.delete(val, True)
                self.assertIsNotNone(self.test_list.get_head())
                self.assertIsNotNone(self.test_list.get_tail())
                self.assertEqual(len(self.test_list), test_list_len)

    def test_large_singleval_list_by_deleting_existing_val(self) -> None:
        ''' Tests deleting large list with single value. Result must be empty list. '''
        test_list_len : int = 1000
        val : int = 5
        for _ in range(test_list_len):
            self.test_list.insert(Node(val), None, True)
        self.test_list.delete(val, True)
        self.assertIsNone(self.test_list.get_head())
        self.assertIsNone(self.test_list.get_tail())
        self.assertEqual(len(self.test_list), 0)

    @parametrize('repeat_times', range(100))
    def test_large_random_list_by_deleting_existing_val(self, repeat_times : int) -> None:
        ''' Tests deleting non-existent value from a large list of random values. '''
        list_len : int = 1000
        val : int = 0
        # Position where to_be_deleted value will be inserted:
        # Head.
        # Right after the head node.
        # Random place between second and tail nodes.
        # Tail.
        val_position_list : list[int] = [0, 1, randint(2, list_len - 2), list_len - 1]
        insert_pos_list : list[int] = sample(val_position_list, randint(0, 4))

        # Fill list with random values from 1 to 100, except positions
        # that are in the insert_position_list.
        for i in range(list_len):
            self.test_list.insert(Node(val if i in insert_pos_list else randint(1, 100)),
                None, True)
        self.test_list.delete(val, True)
        self.assertIsNotNone(self.test_list.get_head())
        self.assertIsNotNone(self.test_list.get_tail())
        self.assertEqual(len(self.test_list),
            list_len if not insert_pos_list else list_len - len(insert_pos_list))

        val_list : list[Node] = self.test_list.find_all(val)
        self.assertEqual(val_list, [])

class LinkedListCleanTests(unittest.TestCase):
    ''' Tests LinkedList clean() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList = LinkedList()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        del self.test_list

    def check(self) -> None:
        ''' Checks list state after clean(). List length must be 0.'''
        self.assertEqual(len(self.test_list), 0)

    def test_empty_list(self) -> None:
        ''' Tests cleaning empty list. '''
        self.test_list.clean()
        self.check()

    def test_single_node_list(self) -> None:
        ''' Tests cleaning list with only one Node. '''
        self.test_list.insert(Node(0))
        self.test_list.clean()
        self.check()

    def test_large_random_list(self) -> None:
        ''' Tests cleaning large list with random values. '''
        for _ in range(1000):
            self.test_list.insert(Node(randint(1, 100)))
        self.test_list.clean()
        self.check()

class LinkedListFindTests(unittest.TestCase):
    ''' Tests LinkedList find() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList = LinkedList()
        self.test_list_len : int = 0
        self.result : Node = None

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        del self.test_list
        self.result = None

    def save_list_state(self) -> None:
        ''' Saves current list length, Head and Tail. '''
        self.test_list_len : int = len(self.test_list)


    def check(self, test_result : Node) -> None:
        ''' Checks list state. It's length must be the same. '''
        self.assertEqual(len(self.test_list), self.test_list_len)
        self.assertIs(self.result, test_result)

    def test_empty_list(self) -> None:
        ''' Tests empty list. Nothing must be found. '''
        self.result = self.test_list.find(0)
        self.check(None)

    def test_single_node_list_by_finding_non_existing_val(self) -> None:
        ''' Tests list with single node. Nothing must be found. '''
        self.test_list.insert(Node(0))
        self.save_list_state()
        self.result = self.test_list.find(1)
        self.check(None)

    def test_single_node_list_by_finding_existing_val(self) -> None:
        ''' Tests list with single node. Exactly one value must be found. '''
        node : Node = Node(0)
        self.test_list.insert(node)
        self.save_list_state()
        self.result = self.test_list.find(0)
        self.check(node)

    def test_large_random_list(self) -> None:
        ''' Test large list with random values. Tries to find random value. '''
        for _ in range(100):
            with self.subTest():
                val : int = randint(0, 10)
                val_node : Node = None
                for _ in range(1000):
                    node : Node = Node(randint(1, 11))
                    self.test_list.insert(node, None, True)
                    if node.value == val and \
                        val_node is None: # Add first occurence of val to control list
                        val_node = node
                self.save_list_state()
                self.result = self.test_list.find(val)
                self.check(val_node)
                self.test_list.clean()
                val_node = None

class LinkedListFindAllTests(unittest.TestCase):
    ''' Tests LinkedList find_all() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList = LinkedList()
        self.test_list_len : int = 0
        self.test_list_head : Node = None
        self.test_list_tail : Node = None
        self.result_list : list[Node] = []

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        del self.test_list
        self.result_list = []

    def save_list_state(self) -> None:
        ''' Saves current list length, Head and Tail. '''
        self.test_list_len : int = len(self.test_list)


    def check(self) -> None:
        ''' Checks list state. It's length must be the same. '''
        self.assertEqual(len(self.test_list), self.test_list_len)

    def test_empty_list(self) -> None:
        ''' Tests empty list. Nothing must be found. '''
        self.result_list = self.test_list.find_all(0)
        self.check()
        self.assertEqual(self.result_list, [])

    def test_single_node_list_by_finding_non_existing_val(self) -> None:
        ''' Tests list with single node. Nothing must be found. '''
        self.test_list.insert(Node(0))
        self.save_list_state()
        self.result_list = self.test_list.find_all(1)
        self.check()
        self.assertEqual(self.result_list, [])

    def test_single_node_list_by_finding_existing_val(self) -> None:
        ''' Tests list with single node. Exactly one value must be found. '''
        self.test_list.insert(Node(0))
        self.save_list_state()
        self.result_list = self.test_list.find_all(0)
        self.check()
        self.assertIs(self.result_list[0], self.test_list.find(0))

    def test_large_random_list(self) -> None:
        ''' Test large list with random values. Tries to find random value. '''
        for _ in range(100):
            with self.subTest():
                val : int = randint(0, 10)
                for _ in range(1000):
                    node : Node = Node(randint(1, 10))
                    self.test_list.insert(node, None, True)
                    if node.value == val: # Add node to control result list
                        self.result_list.append(node)
                self.save_list_state()
                result : list[Node] = self.test_list.find_all(val)
                self.check()
                self.assertEqual(self.result_list, result)
                self.test_list.clean()
                self.result_list = []

class LinkedListLenTests(unittest.TestCase):
    ''' Tests LinkedList __len__() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList = LinkedList()
        self.test_list_len : int = 0
        self.result_len : int = -1
        self.assertEqual(len(self.test_list), 0)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        self.assertEqual(len(self.test_list), 0)
        del self.test_list

    def save_list_state(self, list_len : int) -> None:
        ''' Saves current list length. '''
        self.test_list_len : int = list_len

    def check(self) -> None:
        ''' Checks list state. It's length must be the same. '''
        self.assertEqual(self.result_len, self.test_list_len)

    def test_empty_list(self) -> None:
        ''' Tests empty list. '''
        self.save_list_state(0)
        self.result_len = len(self.test_list)
        self.check()

    def test_singleval_list(self) -> None:
        ''' Tests list with only one node. '''
        self.test_list.insert(Node(0))
        self.save_list_state(1)
        self.result_len = len(self.test_list)
        self.check()

    def test_large_random_list(self) -> None:
        ''' Tests large list with random values. '''
        list_len : int = 1000
        for _ in range(list_len):
            self.test_list.insert(Node(randint(1, 100)))
        self.save_list_state(list_len)
        self.result_len = len(self.test_list)
        self.check()

class LinkedListInsertTests(unittest.TestCase):
    ''' Test LinkedList insert() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList = LinkedList()
        self.head : Node = None
        self.tail : Node = None
        self.list_len : int = 0
        self.inserted_values_list : list[int] = []
        self.result_flag : bool

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        del self.test_list
        self.head = None
        self.tail = None
        self.list_len = 0
        self.inserted_values_list = []

    def check(self, result_flag : bool) -> None:
        ''' Checks if list len is correct.
            Also checks expected result from insert, and order and values of node. '''
        self.assertEqual(self.result_flag, result_flag)
        self.assertEqual(self.list_len, len(self.test_list))
        self.assertIs(self.head, self.test_list.get_head())
        self.assertIs(self.tail, self.test_list.get_tail())
        i : int = 0
        for node in self.test_list:
            self.assertEqual(self.inserted_values_list[i], node.value)
            i += 1

    def test_empty_list_by_inserting_none(self) -> None:
        ''' Tests empty list with before = false and before = true.
            Independently, nothing must be inserted. Function must return false. '''
        insert_arg_list : list[tuple(Node, Node, bool)] = [(None, None, False), (None, None, True)]
        for args in insert_arg_list:
            with self.subTest(new_node = args[0], insertion_node = args[1], flag = args[2]):
                self.result_flag = False
                self.check(self.test_list.insert(args[0], args[1], args[2]))

    def test_empty_list_with_false_flag(self) -> None:
        ''' Tests empty list with before = false. '''
        node : Node = Node(0)
        self.head = self.tail = node
        self.list_len += 1
        self.inserted_values_list.append(0)
        self.result_flag = True
        self.check(self.test_list.insert(node, None))

    def test_empty_list_with_true_flag(self) -> None:
        ''' Tests empty list with before = true. '''
        node : Node = Node(0)
        self.head = self.tail = node
        self.inserted_values_list.append(0)
        self.list_len = 1
        self.result_flag = True
        self.check(self.test_list.insert(node, None))

    def test_single_node_list_by_inserting_none(self) -> None:
        ''' Tests list with single node. Tests following cases:
            1) Insertion node = None and before = false.
            2) Insertion node = None and before = true.
            3) Insertion node = single node and before = false.
            4) Insertion node = single node and before = true.
            In all cases, nothing must be inserted, function mustrreturn false. '''
        node : Node = Node(0)
        self.head = self.tail = node
        self.list_len = 1
        self.test_list.insert(node)
        self.inserted_values_list.append(0)
        insert_arg_list : list[tuple(Node, Node, bool)] = [(None, None, False), (None, None, True),
            (None, node, False), (None, node, True)]
        for args in insert_arg_list:
            with self.subTest(new_node = args[0], insertion_node = args[1], flag = args[2]):
                self.result_flag = False
                self.check(self.test_list.insert(args[0], args[1], args[2]))

    def test_single_node_list_by_inserting_before_none_node(self) -> None:
        ''' Tests list with single node. 
            Insertion_node = None and after = false.
            Node must be inserted in head. '''
        head_node : Node = Node(0)
        tail_node : Node = Node(1)
        self.head = head_node
        self.tail = tail_node
        self.list_len = 2
        self.result_flag = True
        self.inserted_values_list.extend([0, 1])
        self.test_list.insert(tail_node)
        self.check(self.test_list.insert(head_node, None))

    def test_single_node_list_by_inserting_after_none_node(self) -> None:
        ''' Tests list with single node. 
            Insertion_node = None and after = true.
            Node must be inserted in tail. '''
        head_node : Node = Node(0)
        tail_node : Node = Node(1)
        self.head = head_node
        self.tail = tail_node
        self.list_len = 2
        self.result_flag = True
        self.inserted_values_list.extend([0, 1])
        self.test_list.insert(head_node)
        self.check(self.test_list.insert(tail_node, None, True))

    def test_single_node_list_by_inserting_before_single_node(self) -> None:
        ''' Tests list with single node. 
            Insertion_node = single node and after = false.
            Node must be inserted in head. '''
        head_node : Node = Node(0)
        tail_node : Node = Node(1)
        self.head = head_node
        self.tail = tail_node
        self.list_len = 2
        self.result_flag = True
        self.inserted_values_list.extend([0, 1])
        self.test_list.insert(tail_node)
        self.check(self.test_list.insert(head_node, self.test_list.get_head()))

    def test_single_node_list_by_inserting_after_single_node(self) -> None:
        ''' Tests list with single node. 
            Insertion_node = single node and after = true.
            Node must be inserted in tail. '''
        head_node : Node = Node(0)
        tail_node : Node = Node(1)
        self.head = head_node
        self.tail = tail_node
        self.list_len = 2
        self.result_flag = True
        self.inserted_values_list.extend([0, 1])
        self.test_list.insert(head_node)
        self.check(self.test_list.insert(tail_node, self.test_list.get_head(), True))

    @parametrize('repeat_times', range(100))
    def test_large_random_list(self, repeat_times) -> None:
        ''' Tests large list with random values. Inserts node at random position. '''
        random_insertions_number : int = 1000
        for i in range(random_insertions_number):
            self.head : Node = self.test_list.get_head()
            self.tail : Node = self.test_list.get_tail()
            insertion_node_pos : int = sample([-1, randint(-1, self.list_len - 1)], 1)[0]
            if self.list_len == 0: # List is empty, no node positions.
                insertion_node_pos = -1
            after : bool = sample([True, False], 1)[0]
            node : Node = sample([None, Node(randint(1, 100))], 1)[0]
            insertion_node : Node = self.test_list.get_head()
            for _ in range(insertion_node_pos): # Get node at position.
                insertion_node = insertion_node.next
            if insertion_node_pos == -1 and not after: # No insertion node, insert in head
                insertion_node = None
                self.head = node
            if insertion_node_pos == -1 and after: # No insertion node, insert in tail
                insertion_node = None
                self.tail = node
            if insertion_node_pos == 0 and not after: # Insert in head.
                self.head = node
            if insertion_node_pos >= 0 and insertion_node_pos == self.list_len - 1 and \
                after: # Insert in tail.
                self.tail = node
            if node is None: # Nothing will be inserted, head and tail don't change.
                self.head = self.test_list.get_head()
                self.tail = self.test_list.get_tail()
            if node is not None and self.list_len == 0: # Inserted node will be head and tail
                self.head = self.tail = node
            with self.subTest(i = i, list_len = self.list_len, insert_pos = insertion_node_pos,
                new_node_is_not_none = bool(node),
                insertion_node_is_not_none = bool(insertion_node),
                after = after):
                self.result_flag = bool(node)
                if node is None: # Nothing will be inserted, check and continue
                    self.check(self.test_list.insert(node, insertion_node, after))
                    continue
                self.list_len += 1
                expected_pos : int = 0
                if insertion_node and after: # Insert value after
                    expected_pos = insertion_node_pos + 1
                if insertion_node and not after: # Insert value before
                    expected_pos = insertion_node_pos
                if (not insertion_node or insertion_node_pos == 0) and not \
                    after: # Insert value as first element
                    expected_pos = 0
                if (not insertion_node or insertion_node_pos == self.list_len - 1) and \
                    after: # Insert value as last element
                    expected_pos = self.list_len
                self.inserted_values_list.insert(expected_pos, node.value)
                self.check(self.test_list.insert(node, insertion_node, after))

class LinkedListIterTests(unittest.TestCase):
    ''' Test LinkedList __iter__() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList = LinkedList()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        del self.test_list

    def test_empty_list(self) -> None:
        ''' Tests empty list. Iterator must be already exhausted. '''
        it : LinkedListIterator = iter(self.test_list)
        self.assertIsNotNone(it)
        self.assertRaises(StopIteration, next, it)

    def test_single_node_list(self) -> None:
        ''' Tests list with single node. Iterator must be exhausted after one __next__().
            __next__() must give list head. '''
        it : LinkedListIterator = iter(self.test_list)
        self.assertIsNotNone(it)
        i : int = 0
        for node in it: # One iteration only, take head.
            self.assertNotEqual(i, 1)
            self.assertIsNotNone(node)
            self.assertIs(node, self.test_list.get_head())
        self.assertRaises(StopIteration, next, it)

    def test_large_random_list_by_summing_its_elements(self) -> None:
        ''' Tests large random list. Then, iterate over it, summing its nodes value. 
            Sum must be exactly as expected from summing those value via python list. '''
        repeat_test_times : int = 100
        list_len : int = 1000
        for _ in range(repeat_test_times):
            val_list : list[int] = []
            sum_py_list : int = 0
            sum_linked_list : int = 0
            for _ in range(list_len):
                val : int = randint(1, 100)
                self.test_list.insert(Node(val), None, True)
                val_list.append(val)
            with self.subTest():
                it : LinkedListIterator = iter(self.test_list)
                self.assertIsNotNone(it)
                for i in range(list_len):
                    sum_py_list += val_list[i]
                    sum_linked_list += next(it).value
                self.assertEqual(sum_py_list, sum_linked_list)
                self.assertRaises(StopIteration, next, it)
            val_list = []
            self.test_list.clean()

class LinkedListGetHeadTests(unittest.TestCase):
    ''' Test LinkedList get_head() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList = LinkedList()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        del self.test_list

    def test_empty_list(self) -> None:
        ''' Tests empty list. Head must be None. '''
        self.assertIsNone(self.test_list.get_head())

    def test_single_node_list(self) -> None:
        ''' Tests list with single node. Head must be that node. '''
        self.test_list.insert(Node(5))
        self.assertIs(next(iter(self.test_list)), self.test_list.get_head())

    def test_large_random_list(self) -> None:
        ''' Tests large list with random values. After every insertion, Head must be correct. '''
        repeat_test_times : int = 100
        list_insertion_number : int = 1000
        for _ in range(repeat_test_times):
            for _ in range(list_insertion_number):
                self.test_list.insert(Node(randint(1, 100)), None, sample([True, False], 1)[0])
                with self.subTest():
                    self.assertIs(next(iter(self.test_list)), self.test_list.get_head())

class LinkedListGetTailTests(unittest.TestCase):
    ''' Test LinkedList get_tail() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList = LinkedList()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        del self.test_list

    def test_empty_list(self) -> None:
        ''' Tests empty list. Tail must be None. '''
        self.assertIsNone(self.test_list.get_tail())

    def test_single_node_list(self) -> None:
        ''' Tests list with single node. Tail must be that node. '''
        self.test_list.insert(Node(5))
        self.assertIs(next(iter(self.test_list)), self.test_list.get_tail())

    def test_large_random_list(self) -> None:
        ''' Tests large list with random values. After every insertion, Tail must be correct. '''
        repeat_test_times : int = 100
        list_insertion_number : int = 1000
        for _ in range(repeat_test_times):
            for _ in range(list_insertion_number):
                self.test_list.insert(Node(randint(1, 100)), None, sample([True, False], 1)[0])
                with self.subTest():
                    self.assertIs(self.test_list.get_head().prev.prev, self.test_list.get_tail())

class LinkedListPopHeadTests(unittest.TestCase):
    ''' Test LinkedList pop_head() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList = LinkedList()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        del self.test_list

    def test_empty_list(self) -> None:
        ''' Tests empty list. Expected "None" return value and len == 0. '''
        self.assertIsNone(self.test_list.pop_head())
        self.assertEqual(len(self.test_list), 0)

    def test_single_node_list(self) -> None:
        ''' Tests list with single node. Must return value of that node.
            Len must be 0. '''
        self.test_list.insert(Node(5))
        self.assertEqual(self.test_list.pop_head(), 5)
        self.assertEqual(len(self.test_list), 0)

    def test_large_random_list(self) -> None:
        ''' Tests large list with random values. After each operation,
            len must shrink by one, returned value must be same that was in head. '''
        repeat_test_times : int = 100
        initial_len : int = 1000
        for _ in range(repeat_test_times):
            for _ in range(initial_len):
                self.test_list.insert(Node(randint(-100, 100)))
            for i in range(initial_len):
                with self.subTest():
                    if len(self.test_list) == 0:
                        self.assertIsNone(self.test_list.pop_head())
                    if len(self.test_list) > 0:
                        value : int = self.test_list.get_head().value
                        self.assertEqual(self.test_list.pop_head(), value)
                    self.assertEqual(len(self.test_list), initial_len - i - 1)
            self.test_list.clean()

class LinkedListPopTailTests(unittest.TestCase):
    ''' Test LinkedList pop_tail() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList = LinkedList()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        del self.test_list

    def test_empty_list(self) -> None:
        ''' Tests empty list. Expected "None" return value and len == 0. '''
        self.assertIsNone(self.test_list.pop_tail())
        self.assertEqual(len(self.test_list), 0)

    def test_single_node_list(self) -> None:
        ''' Tests list with single node. Must return value of that node.
            Len must be 0. '''
        self.test_list.insert(Node(5))
        self.assertEqual(self.test_list.pop_tail(), 5)
        self.assertEqual(len(self.test_list), 0)

    def test_large_random_list(self) -> None:
        ''' Tests large list with random values. After each operation,
            len must shrink by one, returned value must be same that was in tail. '''
        repeat_test_times : int = 100
        initial_len : int = 1000
        for _ in range(repeat_test_times):
            for _ in range(initial_len):
                self.test_list.insert(Node(randint(-100, 100)))
            for i in range(initial_len):
                with self.subTest():
                    if len(self.test_list) == 0:
                        self.assertIsNone(self.test_list.pop_tail())
                    if len(self.test_list) > 0:
                        value : int = self.test_list.get_tail().value
                        self.assertEqual(self.test_list.pop_tail(), value)
                    self.assertEqual(len(self.test_list), initial_len - i - 1)
            self.test_list.clean()

def suite() -> unittest.TestSuite:
    ''' Collects all TestCase classes for the current test run. '''
    test_loader : unittest.TestLoader = unittest.TestLoader()
    test_suite : unittest.TestSuite = unittest.TestSuite()
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedListLenTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedListCleanTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedListFindTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedListFindAllTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedListInsertTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedListDeleteFirstOccuredValTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedListDeleteAllOccuredValTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedListIterTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedListGetHeadTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedListGetTailTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedListPopHeadTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedListPopTailTests))
    return test_suite

if __name__ == '__main__':
    runner : unittest.TextTestRunner = unittest.TextTestRunner()
    runner.run(suite())
