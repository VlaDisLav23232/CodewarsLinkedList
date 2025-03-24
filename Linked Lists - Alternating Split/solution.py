"""SOLUTION"""

class Node(object):
    """
    A class to represent a node in a linked list.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """
    A class to represent the context of a linked list.
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """
    Splits a linked list into two linked lists.
    """
    if not head or not head.next:
        raise ValueError
    one = head
    first = one
    two = head.next
    second = two
    while second.next and second.next.next:
        first.next = second.next
        first = first.next
        second.next = first.next
        second = second.next
    if second.next:
        first.next = second.next
        first = first.next
    first.next = None
    second.next = None
    return Context(one, two)
