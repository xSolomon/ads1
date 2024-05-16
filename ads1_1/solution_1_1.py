''' LinkedList realisation. '''
class Node:
    ''' Single list elem. '''
    def __init__(self, v):
        self.value = v
        self.next : Node = None

class LinkedList:
    ''' Represents multiple forward-linked nodes. '''
    def __init__(self):
        self.head : Node = None
        self.tail : Node = None

    def add_in_tail(self, item : Node) -> None:
        ''' Adds new node in the tail of list. '''
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self) -> None:
        ''' Prints list to the console. '''
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val) -> Node | None:
        ''' Finds first node with proper value and returns it. '''
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val) -> list[Node]:
        ''' Finds all nodes with proper value and return them as python list. '''
        result : list[Node] = []
        current : Node = self.head
        while current is not None:
            if current.value == val:
                result.append(current)
            current = current.next
        return result

    def delete(self, val, all : bool = False) -> None:
        ''' If all is False, deletes first Node with proper value.
            If all is True, deletes all Nodes with proper value. '''
        if self.head is None: # List is empty.
            return

        temp : Node = self.head # Link to the nodes that will be deleted.
        if self.head.value == val: # Need to delete head.
            if not all: # No need to search further, delete and return.
                self.head = temp.next
                if temp is self.tail: # List contains only one node.
                    self.tail = None
                del temp
                return
            delete_head : bool = True
        else:
            delete_head : bool = False

        current : Node = self.head # Current position in list.
        while current.next is not None: # While not reached last node.
            if current.next.value == val: # Found key, delete it.
                temp = current.next
                current.next = current.next.next
                del temp
                if not all: # We must delete only this element, no need to continue.
                    if current.next is None: # Deleted tail, make it correct.
                        self.tail = current
                    return
                break
            current = current.next

        while current.next is not None: # All is True, search for any other keys without break.
            if current.next.value == val: # Found key, delete it.
                temp = current.next
                current.next = current.next.next
                del temp
                continue # We deleted checked node, no need to advance.
            current = current.next

        # Now current points to the last element, and tail may be broken (was deleted).
        if delete_head: # Handle head deleting.
            temp = self.head
            self.head = temp.next
            del temp
            if self.head is None: # Deleted last element in the list, fix tail and return.
                self.tail = None
                return
        if current is not self.tail: # Tail is broken, fix it.
            self.tail = current

    def clean(self) -> None:
        ''' Deletes all nodes in the list. '''
        current : Node = self.head
        while current is not None:
            current = current.next
            del self.head
            self.head = current
        self.tail = None

    def len(self) -> int:
        ''' Calculates and returns current list len. '''
        list_len : int = 0
        node : Node = self.head
        while node is not None:
            list_len += 1
            node = node.next
        return list_len

    def insert(self, after_node : Node, new_node : Node) -> None:
        ''' Add new node after specified node.
            If after_node is None, inserts new node as the first in the list.'''
        if after_node is None:  # Insert in head.
            new_node.next = self.head
            self.head = new_node
            if self.tail is None: # List was empty before insertion.
                self.tail = self.head
            return
        new_node.next = after_node.next
        after_node.next = new_node
        if self.tail is after_node: # Node was inserted after tail.
            self.tail = new_node




