"""SOLUTION"""

class Node:
    """
    A class to represent a node in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    """
    Pushes a new node to the head of a linked list.
    """
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    """
    Builds a linked list with the values 1, 2, and 3.
    """
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    return head
