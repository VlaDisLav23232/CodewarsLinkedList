"""SOLUTION"""

class Node:
    """
    A class to represent a node in a linked list.
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    """
    Converts a string to a linked list.
    """
    if s  == "None":
        return None
    string = reversed(s.split(" -> ")[:-1])
    head = None

    for value in string:
        head = Node(int(value), head)

    return head
