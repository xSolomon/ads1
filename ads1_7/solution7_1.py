''' Lesson 7 tasks 1-6 solution. '''

class Node:
    ''' List element, containing data and links two next and previous nodes. '''
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    ''' Doubly linked list in which all nodes are ordered in ascending or
        descending way. '''
    def __init__(self, asc : bool):
        self.head : Node = None
        self.tail : Node = None
        self.__len : int = 0
        self.__ascending : bool = asc

    def compare(self, v1, v2) -> int:
        ''' Performs three-way comparison. '''
        if v1 > v2:
            return 1
        return -1 if v1 < v2 else 0

    def add(self, value) -> None:
        ''' Inserts new node in list, depending of list's sorting order. '''
        if self.len() == 0:
            self.__len += 1
            self.head = self.tail = Node(value)
            return
        current : Node = self.head
        continue_search : int = 1 if self.__ascending else -1
        while current is not None:
            if self.compare(value, current.value) != continue_search:
                break
            current = current.next
        self.__len += 1
        if current is None:
            current = Node(value)
            current.prev = self.tail
            self.tail.next = current
            self.tail = current
            return
        if current is self.head:
            current = Node(value)
            current.next = self.head
            self.head.prev = current
            self.head = current
            return
        new_node = Node(value)
        new_node.next = current
        new_node.prev = current.prev
        current.prev = new_node
        new_node.prev.next = new_node

    def find(self, val) -> Node | None:
        ''' Returns first node containing given value. '''
        current : Node = self.head
        continue_search : int = 1 if self.__ascending else -1
        while current is not None:
            if self.compare(val, current.value) != continue_search:
                break
            current = current.next
        return None if current is None or self.compare(val, current.value) != 0 else current

    def delete(self, val) -> None:
        ''' Deletes first occurence of val in list. '''
        if self.len() == 0:
            return
        current : Node = self.head
        while current is not None:
            if current.value == val:
                break
            current = current.next
        if current is None:
            return
        self.__len -= 1
        if self.head is self.tail:
            self.head = self.tail = None
            del current
            return
        if current is self.head:
            self.head = current.next
            self.head.prev = None
            del current
            return
        if current is self.tail:
            self.tail = current.prev
            self.tail.next = None
            del current
            return
        current.next.prev = current.prev
        current.prev.next = current.next
        del current

    def clean(self, asc : bool) -> None:
        ''' Deletes all nodes. Also allows to change element order from
            ascending to descending and vice versa. '''
        self.__ascending = asc
        current = self.head
        while current is not None:
            current = current.next
            del self.head
            self.head = current
        self.tail = None
        self.__len = 0


    def len(self) -> int:
        ''' Returns current list length. '''
        return self.__len

    def get_all(self) -> list[Node]:
        ''' Returns python list containing all nodes. '''
        r : list[Node] = []
        node : Node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    ''' Special version of Ordered list for strings. '''
    def __init__(self, asc : bool):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1 : str, v2 : str) -> int:
        ''' Performs three-way comparison for two strings. '''
        for i in range(min(len(v1), len(v2))):
            c_cmp_result : int = super().compare(v1[i], v2[i])
            if c_cmp_result == 1:
                return 1
            if c_cmp_result == -1:
                return -1
        if len(v1) == len(v2):
            return 0
        return 1 if len(v1) > len(v2) else -1







