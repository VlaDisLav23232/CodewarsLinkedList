"""SOLUTION"""

class Node(object):
    """
    A class to represent a node in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """
    Removes duplicates from a sorted linked list.
    """
    if head is None:
        return None
    current = head
    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next if current.next.next is not None else None
        else:
            current = current.next
    return head
