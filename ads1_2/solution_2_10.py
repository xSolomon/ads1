
''' Doubly linked, cycled list with dummy node realisation. '''

class NodeBase:
    ''' Base Node, contains no data. '''
    def __init__(self):
        self.next : NodeBase = None
        self.prev : NodeBase = None

class Node(NodeBase):
    ''' Node with data. '''
    def __init__(self, v):
        super().__init__()
        self.value = v

class LinkedListIterator:
    ''' Implements iterator protocol for LinkedList. '''
    def __init__(self, linked_list : 'LinkedList3'):
        self.head : NodeBase = linked_list._head
        self.current : NodeBase = self.head.next

    def __iter__(self) -> 'LinkedListIterator':
        return self

    def __next__(self):
        ''' Returns next value in the list. '''
        if self.current is self.head:
            raise StopIteration
        self.current = self.current.next
        return self.current.prev

class LinkedList3:
    ''' Represents circular LinkedList with dummy node. '''
    def __init__(self):
        self._head : NodeBase = NodeBase()
        self._head.next = self._head
        self._head.prev = self._head
        self._len : int = 0

    @staticmethod
    def invariant(linked_list_method):
        ''' If debug, checks LinkedList invariant after any of its methods call. '''
        def call_method_and_check_class_invariant(self, *args, **kwargs):
            result = linked_list_method(self, *args, **kwargs)
            if __debug__:
                self.check_class_invariant()
            return result
        return call_method_and_check_class_invariant

    def check_class_invariant(self) -> None:
        ''' Checks LinkedList invariant:
            1) List length is non-negative.
            2) List head is not None.
            3) List head is instance of NodeBase (dummy node)
            4) For every list node, predecessor of its successor and
            successor of its predeccessor must be same node. '''
        assert self._len >= 0
        assert self._head is not None
        assert not issubclass(type(self._head), Node)
        current : NodeBase = self._head
        assert current.next is not None
        assert current.prev is not None
        while True:
            assert current.next.prev is current
            assert current.prev.next is current
            current = current.next
            assert current.next is not None
            if current is self._head:
                break

    @invariant
    def __iter__(self) -> LinkedListIterator:
        ''' Returns iterator, allowing to traverse list. '''
        return LinkedListIterator(self)

    @invariant
    def __len__(self) -> int:
        ''' Get current length of the list. '''
        list_len : int = self._len
        return list_len

    @invariant
    def get_head(self) -> Node | Node:
        ''' Returns current head. '''
        return self._head.next if self._head.next is not self._head else None

    @invariant
    def get_tail(self) -> Node | Node:
        ''' Returns current head. '''
        return self._head.prev if self._head.prev is not self._head else None

    @invariant
    def insert(self, new_node : Node,  insertion_node : NodeBase = None,
        after : bool = False) -> bool:
        ''' Inserts new node in list.
            If before = false, insert node after given one.
            If before = true, insert node before given one.
            If insertion node is None and before = false, insert in tail.
            If insertion node is None and before = true, insert in head.'''
        if new_node is None: # Nothing to insert.
            return False
        if insertion_node is None and after: # Insert in tail.
            new_node.next = self._head
            new_node.prev = self._head.prev
            self._head.prev.next = new_node
            self._head.prev = new_node
            self._len += 1
            return True
        if insertion_node is None and not after: # Insert in head.
            new_node.prev = self._head
            new_node.next = self._head.next
            self._head.next.prev = new_node
            self._head.next = new_node
            self._len += 1
            return True
        if not after: # Insert before given node.
            new_node.next = insertion_node
            new_node.prev = insertion_node.prev
            insertion_node.prev.next = new_node
            insertion_node.prev = new_node
        else: # Insert after given node.
            new_node.prev = insertion_node
            new_node.next = insertion_node.next
            insertion_node.next.prev = new_node
            insertion_node.next = new_node
        self._len += 1
        return True

    @invariant
    def delete(self, val, delete_all : bool = False) -> None:
        ''' If delete_all = false, deletes first occurence of val in list.
            If delete_all = true, deletes all occurences of val in list. '''
        current : NodeBase = self._head
        while current.next is not self._head:
            if current.next.value == val: # Found first occurence, delete it.
                current.next = current.next.next
                del current.next.prev
                current.next.prev = current
                self._len -= 1
                break
            current = current.next
        if not delete_all:  # One node with val was deleted or no value was found
            return
        while current.next is not self._head:
            if current.next.value == val: # Found another occurence, delete it.
                current.next = current.next.next
                del current.next.prev
                current.next.prev = current
                self._len -= 1
                continue # Cause node was deleted, we don't advance.
            current = current.next

    @invariant
    def find(self, val) -> Node | None:
        ''' Finds first occurence of val in list and returns its node.
            If no node with this key, returns None. '''
        current : NodeBase = self._head
        while (current := current.next) is not self._head:
            if current.value == val: # Found key, return node.
                return current
        return None

    @invariant
    def find_all(self, val) -> list[Node]:
        ''' Finds all occurence of key in LinkedList.
            Returns python list of nodes with value = val. '''
        result : list[Node] = []
        current : NodeBase = self._head
        while (current := current.next) is not self._head:
            if current.value == val: # Found key, add node to the resulting list.
                result.append(current)
        return result

    @invariant
    def clean(self) -> None:
        ''' Delete every node in the list. '''
        current : NodeBase = self._head
        while current.next is not self._head:
            current.next = current.next.next
            del current.next.prev
            current.next.prev = current
            self._len -= 1

    @invariant
    def print_all_nodes(self) -> None:
        ''' Print list to the console. '''
        for node in self:
            print(node.value, end = ' <-> ')
        print('End of list.')
