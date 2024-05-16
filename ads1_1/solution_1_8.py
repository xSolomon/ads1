''' Solution 1.8. '''

from solution_1_1 import LinkedList, Node

def merge_lists_by_adding_their_elements(first : LinkedList,
    second : LinkedList) -> list[LinkedList, bool]:
    ''' For lists of the same length, merge them in one.
        Every node value will be sum of values from corresponding nodes of arg lists.
        If length is not the same, resulting LinkedList will be empty. 
        Second value in return-list indicates if work is successfull. '''
    result : LinkedList = LinkedList()
    if first.len() != second.len():
        return [result, False]
    first_current : Node = first.head
    second_current : Node = second.head
    while first_current is not None:
        result.add_in_tail(Node(first_current.value + second_current.value))
        first_current = first_current.next
        second_current = second_current.next
    return [result, True]
