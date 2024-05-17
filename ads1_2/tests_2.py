''' Tests for LinkedList2. '''

import unittest
from random import randint, sample
from functools import reduce
from parametrize import parametrize
from solution_2 import Node, LinkedList2

class LinkedList2DeleteFirstOccuredValTests(unittest.TestCase):
    ''' Tests for LinkedList2 delete() function, with flag all=false. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList2 = LinkedList2()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        self.assertEqual(self.test_list.len(), 0)
        del self.test_list

    def test_empty_list(self) -> None:
        ''' Tests empty list. '''
        self.test_list.delete(13)
        self.assertIsNone(self.test_list.head)
        self.assertIsNone(self.test_list.tail)
        self.assertEqual(self.test_list.len(), 0)

    @parametrize('node_val, val_to_delete', [(128, 64), (128, 127), (0, 1), (-1, 0)])
    def test_one_elem_list_by_deleting_non_existing_val(self, node_val : int,
        val_to_delete : int) -> None:
        ''' Tests list with single node. Tries to delete value that is not present in the list.
            Nothing must be deleted. '''
        self.test_list.add_in_tail(Node(node_val))
        self.test_list.delete(val_to_delete)
        self.assertIsNotNone(self.test_list.head)
        self.assertIsNotNone(self.test_list.tail)
        self.assertEqual(self.test_list.len(), 1)
        self.assertEqual(self.test_list.head.value, node_val)

    @parametrize('val', [128, 0, -1, 64])
    def test_one_elem_list_by_deleting_existing_val(self, val : int) -> None:
        ''' Tests list with single node. Tries to delete value that is present in the list. 
            Resulting list must be empty. '''
        self.test_list.add_in_tail(Node(val))
        self.test_list.delete(val)
        self.assertEqual(self.test_list.len(), 0)
        self.assertIsNone(self.test_list.head)
        self.assertIsNone(self.test_list.tail)

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
            self.test_list.add_in_tail(Node(val if i in insert_pos_list else randint(1, 100)))
        self.test_list.delete(val)
        self.assertIsNotNone(self.test_list.head)
        self.assertIsNotNone(self.test_list.tail)
        self.assertEqual(self.test_list.len(), (list_len if not insert_pos_list else list_len - 1))

        val_list : list[Node] = self.test_list.find_all(val)
        if len(insert_pos_list) <= 1:
            self.assertEqual(val_list, [])
        else:
            self.assertEqual(len(val_list), len(insert_pos_list) - 1)
            self.assertTrue(reduce(lambda x, y : x and (y.value == val), val_list, True))

class LinkedList2DeleteAllOccuredValTests(unittest.TestCase):
    ''' Tests for LinkedList2 delete() function, with flag all=false. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList2 = LinkedList2()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        self.assertEqual(self.test_list.len(), 0)
        del self.test_list

    def test_empty_list(self) -> None:
        ''' Tests empty list. '''
        self.test_list.delete(13, True)
        self.assertIsNone(self.test_list.head)
        self.assertIsNone(self.test_list.tail)
        self.assertEqual(self.test_list.len(), 0)

    @parametrize('node_val, val_to_delete', [(128, 64), (128, 127), (0, 1), (-1, 0)])
    def test_one_elem_list_by_deleting_non_existing_val(self, node_val : int,
        val_to_delete : int) -> None:
        ''' Tests list with single node. Tries to delete value that is not present in the list.
            Nothing must be deleted. '''
        self.test_list.add_in_tail(Node(node_val))
        self.test_list.delete(val_to_delete, True)
        self.assertIsNotNone(self.test_list.head)
        self.assertIsNotNone(self.test_list.tail)
        self.assertEqual(self.test_list.len(), 1)
        self.assertEqual(self.test_list.head.value, node_val)

    @parametrize('val', [128, 0, -1, 64])
    def test_one_elem_list_by_deleting_existing_val(self, val : int) -> None:
        ''' Tests list with single node. Tries to delete value that is present in the list. 
            Resulting list must be empty. '''
        self.test_list.add_in_tail(Node(val))
        self.test_list.delete(val, True)
        self.assertEqual(self.test_list.len(), 0)
        self.assertIsNone(self.test_list.head)
        self.assertIsNone(self.test_list.tail)

    def test_large_list_by_deleting_non_existing_vals(self) -> None:
        ''' Tests deleting non-existent value from a large list of random values. '''
        val_list : list[int] = [-1, 101, 102, 103, 0]
        test_list_len : int = 1000
        for _ in range(test_list_len):
            self.test_list.add_in_tail(Node(randint(1, 100)))
        for val in val_list:
            with self.subTest():
                self.test_list.delete(val, True)
                self.assertIsNotNone(self.test_list.head)
                self.assertIsNotNone(self.test_list.tail)
                self.assertEqual(self.test_list.len(), test_list_len)

    def test_large_singleval_list_by_deleting_existing_val(self) -> None:
        ''' Tests deleting large list with single value. Result must be empty list. '''
        test_list_len : int = 1000
        val : int = 5
        for _ in range(test_list_len):
            self.test_list.add_in_tail(Node(val))
        self.test_list.delete(val, True)
        self.assertIsNone(self.test_list.head)
        self.assertIsNone(self.test_list.tail)
        self.assertEqual(self.test_list.len(), 0)

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
            self.test_list.add_in_tail(Node(val if i in insert_pos_list else randint(1, 100)))
        self.test_list.delete(val, True)
        self.assertIsNotNone(self.test_list.head)
        self.assertIsNotNone(self.test_list.tail)
        self.assertEqual(self.test_list.len(),
            list_len if not insert_pos_list else list_len - len(insert_pos_list))

        val_list : list[Node] = self.test_list.find_all(val)
        self.assertEqual(val_list, [])

class LinkedList2CleanTests(unittest.TestCase):
    ''' Tests LinkedList2 clean() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList2 = LinkedList2()
        self.assertIsNone(self.test_list.head)
        self.assertIsNone(self.test_list.tail)
        self.assertEqual(self.test_list.len(), 0)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        self.assertEqual(self.test_list.len(), 0)
        del self.test_list

    def check(self) -> None:
        ''' Checks list state after clean().
            Tail and Head must be None, and list length is 0. '''
        self.assertIsNone(self.test_list.head)
        self.assertIsNone(self.test_list.tail)
        self.assertEqual(self.test_list.len(), 0)

    def test_empty_list(self) -> None:
        ''' Tests cleaning empty list. '''
        self.test_list.clean()
        self.check()

    def test_single_node_list(self) -> None:
        ''' Tests cleaning list with only one Node. '''
        self.test_list.add_in_tail(Node(0))
        self.test_list.clean()
        self.check()

    def test_large_random_list(self) -> None:
        ''' Tests cleaning large list with random values. '''
        for _ in range(1000):
            self.test_list.add_in_tail(Node(randint(1, 100)))
        self.test_list.clean()
        self.check()

class LinkedList2FindTests(unittest.TestCase):
    ''' Tests LinkedList2 find() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList2 = LinkedList2()
        self.test_list_len : int = 0
        self.test_list_head : Node = None
        self.test_list_tail : Node = None
        self.result : Node = None
        self.assertIsNone(self.test_list.head)
        self.assertIsNone(self.test_list.tail)
        self.assertEqual(self.test_list.len(), 0)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        self.assertEqual(self.test_list.len(), 0)
        del self.test_list
        self.result = None

    def save_list_state(self) -> None:
        ''' Saves current list length, Head and Tail. '''
        self.test_list_len : int = self.test_list.len()
        self.test_list_head : Node = self.test_list.head
        self.test_list_tail : Node = self.test_list.tail


    def check(self) -> None:
        ''' Checks list state. It's length must be the same.
            Also Head and Tail mustn't change. '''
        self.assertEqual(self.test_list.len(), self.test_list_len)
        self.assertEqual(self.test_list.head, self.test_list_head)
        self.assertEqual(self.test_list.tail, self.test_list_tail)

    def test_empty_list(self) -> None:
        ''' Tests empty list. Nothing must be found. '''
        self.result = self.test_list.find(0)
        self.check()
        self.assertEqual(self.result, None)

    def test_single_node_list_by_finding_non_existing_val(self) -> None:
        ''' Tests list with single node. Nothing must be found. '''
        self.test_list.add_in_tail(Node(0))
        self.save_list_state()
        self.result = self.test_list.find(1)
        self.check()
        self.assertIs(self.result, None)

    def test_single_node_list_by_finding_existing_val(self) -> None:
        ''' Tests list with single node. Exactly one value must be found. '''
        self.test_list.add_in_tail(Node(0))
        self.save_list_state()
        self.result = self.test_list.find(0)
        self.check()
        self.assertIs(self.result, self.test_list.head)

    def test_large_list(self) -> None:
        ''' Test large list with random values. Tries to find random value. '''
        for _ in range(100):
            with self.subTest():
                val : int = randint(0, 10)
                for _ in range(1000):
                    self.test_list.add_in_tail(Node(randint(1, 10)))
                    if self.test_list.tail.value == val and \
                        self.result is None: # Add first occurence of val to control list
                        self.result = self.test_list.tail
                self.save_list_state()
                result : Node = self.test_list.find(val)
                self.check()
                self.assertIs(self.result, result)
                self.test_list.clean()
                self.result = None

class LinkedList2FindAllTests(unittest.TestCase):
    ''' Tests LinkedList2 find_all() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList2 = LinkedList2()
        self.test_list_len : int = 0
        self.test_list_head : Node = None
        self.test_list_tail : Node = None
        self.result_list : list[Node] = []
        self.assertIsNone(self.test_list.head)
        self.assertIsNone(self.test_list.tail)
        self.assertEqual(self.test_list.len(), 0)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        self.assertEqual(self.test_list.len(), 0)
        del self.test_list
        self.result_list = []

    def save_list_state(self) -> None:
        ''' Saves current list length, Head and Tail. '''
        self.test_list_len : int = self.test_list.len()
        self.test_list_head : Node = self.test_list.head
        self.test_list_tail : Node = self.test_list.tail


    def check(self) -> None:
        ''' Checks list state. It's length must be the same.
            Also Head and Tail mustn't change. '''
        self.assertEqual(self.test_list.len(), self.test_list_len)
        self.assertEqual(self.test_list.head, self.test_list_head)
        self.assertEqual(self.test_list.tail, self.test_list_tail)

    def test_empty_list(self) -> None:
        ''' Tests empty list. Nothing must be found. '''
        self.result_list = self.test_list.find_all(0)
        self.check()
        self.assertEqual(self.result_list, [])

    def test_single_node_list_by_finding_non_existing_val(self) -> None:
        ''' Tests list with single node. Nothing must be found. '''
        self.test_list.add_in_tail(Node(0))
        self.save_list_state()
        self.result_list = self.test_list.find_all(1)
        self.check()
        self.assertEqual(self.result_list, [])

    def test_single_node_list_by_finding_existing_val(self) -> None:
        ''' Tests list with single node. Exactly one value must be found. '''
        self.test_list.add_in_tail(Node(0))
        self.save_list_state()
        self.result_list = self.test_list.find_all(0)
        self.check()
        self.assertIs(self.result_list[0], self.test_list.find(0))

    def test_large_list(self) -> None:
        ''' Test large list with random values. Tries to find random value. '''
        for _ in range(100):
            with self.subTest():
                val : int = randint(0, 10)
                for _ in range(1000):
                    self.test_list.add_in_tail(Node(randint(1, 10)))
                    if self.test_list.tail.value == val: # Add node to control result list
                        self.result_list.append(self.test_list.tail)
                self.save_list_state()
                result : list[Node] = self.test_list.find_all(val)
                self.check()
                self.assertEqual(self.result_list, result)
                self.test_list.clean()
                self.result_list = []

class LinkedList2LenTests(unittest.TestCase):
    ''' Tests LinkedList2 len() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList2 = LinkedList2()
        self.test_list_len : int = 0
        self.result_len : int = -1
        self.test_list_head : Node = None
        self.test_list_tail : Node = None
        self.assertIsNone(self.test_list.head)
        self.assertIsNone(self.test_list.tail)
        self.assertEqual(self.test_list.len(), 0)

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        self.assertEqual(self.test_list.len(), 0)
        del self.test_list

    def save_list_state(self, list_len : int) -> None:
        ''' Saves current list length, Head and Tail. '''
        self.test_list_len : int = list_len
        self.test_list_head : Node = self.test_list.head
        self.test_list_tail : Node = self.test_list.tail

    def check(self) -> None:
        ''' Checks list state. It's length must be the same.
            Also Head and Tail mustn't change. '''
        self.assertEqual(self.result_len, self.test_list_len)
        self.assertEqual(self.test_list.head, self.test_list_head)
        self.assertEqual(self.test_list.tail, self.test_list_tail)

    def test_empty_list(self) -> None:
        ''' Tests empty list. '''
        self.save_list_state(0)
        self.result_len = self.test_list.len()
        self.check()

    def test_singleval_list(self) -> None:
        ''' Tests list with only one node. '''
        self.test_list.add_in_tail(Node(0))
        self.save_list_state(1)
        self.result_len = self.test_list.len()
        self.check()

    def test_large_random_list(self) -> None:
        ''' Tests large list with random values. '''
        for _ in range(1000):
            self.test_list.add_in_tail(Node(randint(1, 100)))
        self.save_list_state(1000)
        self.result_len = self.test_list.len()
        self.check()

class LinkedList2InsertTests(unittest.TestCase):
    ''' Test LinkedList2 insert() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList2 = LinkedList2()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        self.assertEqual(self.test_list.len(), 0)
        del self.test_list

    def check(self, list_len : int, head : Node, tail : Node) -> None:
        ''' Checks if list len, Head and Tail are correct. '''
        self.assertEqual(self.test_list.len(), list_len)
        self.assertIs(self.test_list.head, head)
        self.assertIs(self.test_list.tail, tail)

    def test_empty_list(self) -> None:
        ''' Tests empty list. Node must be inserted in head. '''
        node : Node = Node(0)
        self.test_list.insert(None, node)
        self.check(1, node, node)

    def test_single_node_list_by_inserting_after_1(self) -> None:
        ''' Tests list with single node. Node must be inserted in tail. AfterNode = None. ''' 
        node : Node = Node(0)
        head_node : Node = Node(1)
        self.test_list.add_in_tail(head_node)
        self.test_list.insert(None, node)
        self.check(2, head_node, node)

    def test_single_node_list_by_inserting_after_2(self) -> None:
        ''' Tests list with single node. Node must be inserted in tail. AfterNode = Tail. ''' 
        node : Node = Node(0)
        head_node : Node = Node(1)
        self.test_list.add_in_tail(head_node)
        self.test_list.insert(self.test_list.tail, node)
        self.check(2, head_node, node)

    def test_large_random_list(self) -> None:
        ''' Tests large list with random values. Inserts node at random position. '''
        random_insertions_number : int = 10000
        list_len : int = 0
        for _ in range(random_insertions_number):
            insert_pos : int = randint(0, list_len)
            with self.subTest(pos = insert_pos, list_len = list_len):
                after_node : Node = self.test_list.head
                head_node : Node = self.test_list.head
                tail_node : Node = self.test_list.tail
                for _ in range(insert_pos - 1):
                    after_node = after_node.next
                node : Node = Node(randint(1, 100))
                if insert_pos == 0:
                    if head_node is None:
                        head_node = node
                    after_node = None
                    tail_node = node
                if insert_pos == list_len:
                    tail_node = node
                self.test_list.insert(after_node, node)
                list_len += 1
                self.check(list_len, head_node, tail_node)

class LinkedList2AddInHeadTests(unittest.TestCase):
    ''' Test LinkedList2 add_in_head() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.test_list : LinkedList2 = LinkedList2()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        self.test_list.clean()
        self.assertEqual(self.test_list.len(), 0)
        del self.test_list

    def check(self, list_len : int, head : Node, tail : Node) -> None:
        ''' Checks if list len, Head and Tail are correct. '''
        self.assertEqual(self.test_list.len(), list_len)
        self.assertIs(self.test_list.head, head)
        self.assertIs(self.test_list.tail, tail)

    def test_empty_list(self) -> None:
        ''' Tests empty list. '''
        node : Node = Node(0)
        self.test_list.add_in_head(node)
        self.check(1, node, node)

    def test_single_node_list_by_inserting_before(self) -> None:
        ''' Tests list with single node.''' 
        node : Node = Node(0)
        tail_node : Node = Node(1)
        self.test_list.add_in_head(tail_node)
        self.test_list.add_in_head(node)
        self.check(2, node, tail_node)

    def test_large_random_list(self) -> None:
        ''' Tests large list with random values. '''
        random_insertions_number : int = 10000
        list_len : int = 0
        self.test_list.add_in_head(Node(randint(1, 100)))
        list_len += 1
        tail_node : Node = self.test_list.tail
        for _ in range(random_insertions_number):
            with self.subTest():
                node : Node = Node(randint(1, 100))
                self.test_list.add_in_head(node)
                list_len += 1
                self.check(list_len, node, tail_node)
                self.assertIs(self.test_list.find(node.value), node)

def suite() -> unittest.TestSuite:
    ''' Collects all TestCase classes for the current test run. '''
    test_loader : unittest.TestLoader = unittest.TestLoader()
    test_suite : unittest.TestSuite = unittest.TestSuite()
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedList2LenTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedList2CleanTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedList2FindTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedList2FindAllTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedList2DeleteFirstOccuredValTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedList2DeleteAllOccuredValTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedList2AddInHeadTests))
    test_suite.addTests(test_loader.loadTestsFromTestCase(LinkedList2InsertTests))
    return test_suite

if __name__ == '__main__':
    runner : unittest.TextTestRunner = unittest.TextTestRunner()
    runner.run(suite())
