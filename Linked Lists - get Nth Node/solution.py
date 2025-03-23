"""SOLUTION"""

class Node(object):
    """
    A class to represent a node in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def get_nth(node, index):
    """
    Returns the Nth node in a linked list.
    """
    if index < 0 or not isinstance(node, Node):
        raise ValueError
    current = node
    for _ in range(index):
        if current.next is not None:
            current = current.next
        else:
            raise ValueError
    return current
