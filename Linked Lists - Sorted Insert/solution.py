"""SOLUTION"""
class Node(object):
    """
    A class to represent a node in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    """
    Inserts a node into a sorted linked list.
    """
    if not isinstance(head, Node):
        return Node(data)
    if head.data > data:
        new_head = Node(data)
        new_head.next = head
        return new_head
    current = head
    while current.next.data < data:
        current = current.next
        if current.next is None:
            break
    to_move = current.next
    current.next = Node(data)
    current.next.next = to_move
    return head
