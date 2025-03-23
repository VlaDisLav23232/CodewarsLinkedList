"""SOLUTION"""

class Node(object):
    """
    A class to represent a node in a linked list.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    """
    Reverses a linked list.
    """
    if not head or not head.next:
        return head

    new_head = reverse(head.next)
    head.next.next = head
    head.next = None

    return new_head
