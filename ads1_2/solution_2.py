''' Doubly linked list realisation. '''

class Node:
    ''' List elem. '''
    def __init__(self, v):
        self.value = v
        self.prev : Node = None
        self.next : Node = None

class LinkedList2:
    ''' Doubly linked list. '''
    def __init__(self):
        self.head : Node = None
        self.tail : Node = None

    def add_in_tail(self, item) -> None:
        ''' Insert new node in the tail. '''
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
            item.next = None
        self.tail = item

    def find(self, val) -> Node | None:
        ''' Find first occurence of val in the list and return link to the Node.
            Returns None if there aren't any.'''
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val) -> list[Node]:
        ''' Find all occurences of val in the list and return as python list.
            Returns empty list if there aren't any. '''
        result : list[Node] = []
        current : Node = self.head
        while current is not None:
            if current.value == val:
                result.append(current)
            current = current.next
        return result

    def delete(self, val, all : bool = False) -> None:
        ''' Deletes first or all occurence (dependent on flag) of val in list. '''
        if self.head is None: # Handle empty list case.
            return

        # Temporary bind head to tail to simplify algorithm
        current : Node = self.tail
        current.next = self.head
        self.head.prev = current
        while current.next is not self.tail: # Check all but last element
            if current.next.value == val: # Found first occurence
                current.next = current.next.next
                del current.next.prev
                current.next.prev = current
                if not all: # No need to search further, break head-tail cycle and return
                    self.head = self.tail.next # Ensure head correctness in case we deleted it
                    self.tail.next = None
                    self.head.prev = None
                    return
                break
            current = current.next

        while current.next is not self.tail: # Check all but last element
            if current.next.value == val: # Found another occurence
                current.next = current.next.next
                del current.next.prev
                current.next.prev = current
                continue # Cause element was deleted, we don't advance
            current = current.next
        self.head = self.tail.next # Ensure head correctness in case we deleted it

        # At this point, all nodes but tail are checked
        # current is one node before tail or tail if list contains only one node
        if current.next.value == val: # Need to delete tail element
            if self.head is self.tail: # Deleting last node
                del self.head
                self.head = self.tail = None
                return
            current.next = current.next.next
            del current.next.prev
            current.next.prev = current
            self.tail = self.head.prev # Fix broken tail
        # Break cycle between head and tail
        self.head.prev = None
        self.tail.next = None

    def clean(self) -> None:
        ''' Delete all Nodes (make list empty). '''
        current : Node = self.head
        while current is not None:
            current = current.next
            del self.head
            self.head = current
        self.tail = None

    def len(self) -> int:
        ''' Calculate current length. '''
        list_len : int = 0
        node : Node = self.head
        while node is not None:
            list_len += 1
            node = node.next
        return list_len

    def insert(self, after_node : Node, new_node : Node) -> None:
        ''' Insert node after given one. If given None and:
            List is empty -> insert in head.
            List is not empty -> insert in tail. '''
        if self.head is None: # Handle empty list case.
            new_node.next = None
            new_node.prev = None
            self.head = self.tail = new_node
            return
        if after_node is None or after_node is self.tail: # Handle in-tail insertion case.
            new_node.Next = None
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return
        new_node.next = after_node.next
        new_node.prev = after_node
        after_node.next = new_node
        new_node.next.prev = new_node

    def add_in_head(self, new_node : Node) -> None:
        ''' Insert new node in the head. '''
        if self.head is None: # Handle empty list case.
            self.tail = new_node
            new_node.next = None
            new_node.prev = None
        else:
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
        self.head = new_node
