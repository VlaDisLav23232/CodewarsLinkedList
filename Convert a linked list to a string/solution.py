"""SOLUTION"""

class Node:
    """
    A class to represent a node in a linked list.
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def stringify(node):
    """
    Converts a linked list to a string.
    """
    current_node = node
    full_str = ""
    while current_node is not None:
        full_str += current_node.data + " -> "
        current_node = node.next
    full_str += "None"
    return full_str
