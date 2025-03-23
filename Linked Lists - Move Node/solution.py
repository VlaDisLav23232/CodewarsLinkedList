"""SOLUTION"""

class Node(object):
    """
    A class to represent a node in a linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """
    A class to represent the context of a linked list.
    """
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """
    Moves a node from the source linked list to the destination linked list.
    """
    node_to_move = source
    new_source = node_to_move.next

    node_to_move.next = dest
    return Context(new_source, node_to_move)
