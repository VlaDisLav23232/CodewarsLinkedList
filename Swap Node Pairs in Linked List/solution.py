"""SOLUTION"""

class Node:
    """
    A class to represent a node in a linked list.
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def swap_pairs(head):
    """
    Swaps every two adjacent nodes in a linked list.
    """
    if not head or not head.next:
        return head

    new_head = head.next
    prev = None
    current = head

    while current and current.next:
        first = current
        second = current.next
        first.next = second.next
        second.next = first

        if prev:
            prev.next = second
        prev = first
        current = first.next

    return new_head
